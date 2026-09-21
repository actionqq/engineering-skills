#!/usr/bin/env python3
"""Export raw case inputs only. This is packaging, not a security sandbox."""
import argparse
import json
import subprocess
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]


def safe_relative(name):
    p = PurePosixPath(name)
    if not name or not p.parts or p.is_absolute() or '..' in p.parts or '\\' in name:
        raise ValueError(f'Invalid fixture path: {name!r}')
    return p


def materialize(case, destination):
    destination = Path(destination).resolve()
    # Validate paths before creating anything; refuse reuse, even an empty folder.
    paths = {name: safe_relative(name) for name in case['files']}
    if case.get('fixture_recipe') not in (None, 'mixed-wip'):
        raise ValueError('Unknown fixture recipe')
    if destination.exists():
        raise FileExistsError(f'Destination already exists: {destination}')
    destination.mkdir(parents=True)
    workspace = destination / 'workspace'
    workspace.mkdir()
    for name, content in case['files'].items():
        p = workspace / paths[name]
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding='utf-8')
    if case.get('fixture_recipe') == 'mixed-wip':
        def git(*args):
            return subprocess.run(['git', *args], cwd=workspace, check=True,
                                  text=True, capture_output=True)
        git('init', '-q')
        git('add', '.')
        git('-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid',
            '-c', 'commit.gpgsign=false', '-c', 'core.hooksPath=/dev/null',
            'commit', '-qm', 'Fixture baseline')
        (workspace / 'tracked.py').write_text('def version():\n    return 2\n')
        git('add', 'tracked.py')
        (workspace / 'tracked.py').write_text('def version():\n    return 3\n')
        (workspace / 'untracked.py').write_text('def allowed(user):\n    return True\n')
    # Deliberately excludes expect, reject, near_miss, skill and capability labels.
    prompt = case['request'] + '\n\n环境说明：' + case['setup'] + '\n\n工作目录：workspace/\n'
    (destination / 'request.md').write_text(prompt, encoding='utf-8')
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('case_id')
    parser.add_argument('destination', type=Path)
    args = parser.parse_args()
    cases = json.loads((ROOT / 'evals/cases.json').read_text())['cases']
    matching = [case for case in cases if case['id'] == args.case_id]
    if not matching:
        parser.error('Unknown case ID')
    try:
        print(materialize(matching[0], args.destination))
    except (ValueError, FileExistsError) as error:
        parser.error(str(error))


if __name__ == '__main__':
    main()
