#!/usr/bin/env python3
"""Validate bundle structure and traceability; does not score model behavior."""
import argparse
import ast
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r'\[[^\]]*\]\(([^)]+)\)')


def validate(root):
    errors = []
    def check(condition, message):
        if not condition:
            errors.append(message)
    manifest = json.loads((root / 'manifest.json').read_text())
    capability_map = manifest['capabilities']
    expected = set(capability_map)
    renamed = manifest.get('renamed_entries', {})
    check(not (set(renamed) & expected), 'Retired names remain active in manifest')
    check(set(renamed.values()) <= expected, 'Rename targets are missing from manifest')
    check(len(set(renamed.values())) == len(renamed), 'Rename targets are ambiguous')
    actual = {p.name for p in (root / 'skills').iterdir() if p.is_dir()}
    check(actual == expected, 'Skill directories differ from manifest')
    all_capabilities = {x for v in capability_map.values() for x in v}
    check(bool(expected), 'Manifest has no entrypoints')
    check(all(capability_map.values()), 'Manifest entry has no capabilities')
    check(sum(map(len, capability_map.values())) == len(all_capabilities),
          'Duplicate capability ownership in manifest')
    references = 0
    instruction_words = {}
    for name in sorted(expected):
        folder = root / 'skills' / name
        skill = folder / 'SKILL.md'
        content = skill.read_text()
        match = re.match(r'^---\n(.*?)\n---\n', content, re.S)
        check(bool(match), f'{name}: missing frontmatter')
        if not match:
            continue
        front = yaml.safe_load(match.group(1))
        check(front.get('name') == name, f'{name}: name mismatch')
        check(bool(front.get('description')), f'{name}: missing description')
        check(len(front.get('description','')) <= 1024, f'{name}: description too long')
        check(not re.search(r'[\u4e00-\u9fff]', content), f'{name}: non-English instruction')
        instruction_words[name] = len(content[match.end():].split())
        ui = yaml.safe_load((folder / 'agents/openai.yaml').read_text())
        check(25 <= len(ui['interface']['short_description']) <= 64, f'{name}: UI description length')
        check(ui.get('policy', {}).get('allow_implicit_invocation', True), f'{name}: implicit discovery disabled')
        check((folder / 'THIRD_PARTY_NOTICES.md').is_file(), f'{name}: missing notices')
        # Traverse only resource links reachable from this Skill, and require closure.
        visited, todo = set(), [skill.resolve()]
        while todo:
            current = todo.pop()
            if current in visited:
                continue
            visited.add(current)
            check(current.is_relative_to(folder.resolve()), f'{name}: resource escapes standalone folder')
            if not current.is_file():
                errors.append(f'Missing resource: {current}')
                continue
            for target in LINK.findall(current.read_text()):
                if '://' in target or target.startswith('#'):
                    continue
                linked = (current.parent / target.split('#')[0]).resolve()
                check(linked.is_file(), f'Broken link in {current}: {target}')
                if linked.suffix == '.md' and linked not in visited:
                    todo.append(linked)
        for ref in (folder / 'references').glob('*.md'):
            references += 1
            check(ref.resolve() in visited, f'{name}: unreachable reference {ref.name}')
            check(not re.search(r'[\u4e00-\u9fff]',ref.read_text()), f'{name}: non-English reference')
        for document in [skill, *(folder / 'references').glob('*.md')]:
            check('/home/seven/' not in document.read_text(), f'{document}: private absolute path')
            check('[TODO:' not in document.read_text(), f'{document}: unfinished placeholder')
    cases_doc = json.loads((root / 'evals/cases.json').read_text())
    # The historical case bank is optional coverage, not an authoring prerequisite.
    # Check every coverage claim it makes without manufacturing cases for new Skills.
    case_capability_map = cases_doc['capabilities']
    for name, capabilities in case_capability_map.items():
        check(name in expected and set(capabilities) <= set(capability_map.get(name, [])),
              'Case capability map has unknown entry or capability: '+name)
    cases = cases_doc['cases']
    ids = [case['id'] for case in cases]
    check(len(ids) == len(set(ids)), 'Duplicate case IDs')
    covered = set()
    for case in cases:
        check(case['skill'] in expected, f"Unknown skill: {case['id']}")
        check(bool(case['expect']) and bool(case['reject']), f"Missing discriminators: {case['id']}")
        check(bool(case.get('near_miss')), f"Missing near-miss: {case['id']}")
        for cap in case['capabilities']:
            check(cap in capability_map.get(case['skill'], []), f"Bad capability: {case['id']}/{cap}")
            check(cap in case_capability_map.get(case['skill'], []),
                  f"Undeclared case coverage: {case['id']}/{cap}")
            covered.add(cap)
        for name, content in case['files'].items():
            if name.endswith('.py'):
                try:
                    ast.parse(content, filename=name)
                except SyntaxError as error:
                    errors.append(f"Fixture syntax: {case['id']}/{name}: {error}")
    check(covered == {x for v in case_capability_map.values() for x in v},
          'Declared case coverage differs from prepared cases')
    queries = json.loads((root / 'evals/discovery.json').read_text())['queries']
    check(len({q['id'] for q in queries}) == len(queries), 'Duplicate discovery query IDs')
    for query in queries:
        check(query['context_case'] in ids, 'Unknown discovery context '+query['id'])
        check(query['expected_primary'] is None or query['expected_primary'] in expected,
              'Unknown discovery entry '+query['id'])
        if 'avoid_forcing' in query:
            check(query['avoid_forcing'] in expected, 'Unknown discovery neighbor '+query['id'])
    host_doc = json.loads((root / 'evals/host-names.json').read_text())
    host_cases = host_doc['cases']
    check(len({c['id'] for c in host_cases}) == len(host_cases), 'Duplicate host-name case IDs')
    required_dimensions = {'native-command', 'native-alias', 'bundled-skill', 'separate-namespaces',
                           'duplicate-sources', 'retired-names', 'similar-names', 'side-effecting-native-command'}
    check(required_dimensions <= {c['dimension'] for c in host_cases}, 'Missing host-name dimensions')
    check({'host_version', 'exact_invocation', 'resolved_source', 'content_sha256',
           'dispatch_or_load_evidence'} <= set(host_doc['required_evidence']),
          'Host-name protocol lacks source-resolution evidence')
    for case in host_cases:
        check(set(case['skills']) <= expected, 'Unknown host-name entry '+case['id'])
        check(bool(case['expect']) and bool(case['reject']), 'Missing host-name discriminators '+case['id'])
    sources = json.loads((root / 'provenance/sources.lock.json').read_text())['sources']
    by_id = {source['id']: source for source in sources}
    for source in sources:
        check(bool(re.fullmatch('[0-9a-f]{40}', source['commit'])), 'Unpinned source '+source['id'])
        check(bool(re.fullmatch('[0-9a-f]{64}', source['sha256'])), 'Missing source hash '+source['id'])
    methods = json.loads((root / 'provenance/method-map.json').read_text())['methods']
    mapped_resources = set()
    for method in methods:
        for source_id in method['sources']:
            check(source_id in by_id, f"Unknown source: {method['id']}")
            check(by_id.get(source_id, {}).get('review_scope') in ('full-text','selected-lines'),
                  f"Method attributed to unread source: {source_id}")
        for destination in method['destinations']:
            check((root / destination).is_file(), 'Missing method destination '+destination)
            mapped_resources.add(destination)
        for case_id in method['eval_cases']:
            check(case_id in ids, 'Unknown method case '+case_id)
    all_refs = {str(p.relative_to(root)) for p in (root / 'skills').glob('*/references/*.md')}
    check(all_refs <= mapped_resources, 'Some references have no method provenance')
    return {'kind':'structural-validation','passed':not errors,'errors':errors,
            'skills':len(expected),'capabilities':len(all_capabilities),'references':references,
            'capabilities_with_prepared_cases':len(covered),
            'capabilities_without_prepared_cases':sorted(all_capabilities - covered),
            'prepared_cases':len(cases),'method_groups':len(methods),'pinned_files':len(sources),
            'prepared_trigger_requests':len(queries),'prepared_host_name_scenarios':len(host_cases),
            'entrypoint_words':instruction_words,
            'limits':'Syntax, local resource closure, declared coverage and source bookkeeping only; no model behavior or quality comparison.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = validate(args.root.resolve())
    text = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if args.output:
        args.output.write_text(text, encoding='utf-8')
    print(text, end='')
    raise SystemExit(0 if result['passed'] else 1)


if __name__ == '__main__':
    main()
