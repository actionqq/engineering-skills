"""Read the base evaluation case bank and its dated fragments."""
import json


def load_case_bank(root):
    eval_dir = root / 'evals'
    bank = json.loads((eval_dir / 'cases.json').read_text(encoding='utf-8'))
    capabilities, cases = bank['capabilities'], bank['cases']
    for path in sorted(eval_dir.glob('cases.*.json')):
        fragment = json.loads(path.read_text(encoding='utf-8'))
        for name, values in fragment.get('capabilities', {}).items():
            merged = capabilities.setdefault(name, [])
            for value in values:
                if value not in merged:
                    merged.append(value)
        cases.extend(fragment.get('cases', []))
    return capabilities, cases
