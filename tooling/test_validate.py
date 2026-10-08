"""Regression checks for optional evaluation coverage and resource integrity."""
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from validate import ROOT, validate


class ValidationCoverageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('skills', 'provenance', 'evals'):
            shutil.copytree(ROOT / name, self.root / name)
        shutil.copy2(ROOT / 'manifest.json', self.root / 'manifest.json')

    def update_case_map(self, name, capabilities):
        path = self.root / 'evals/cases.json'
        data = json.loads(path.read_text())
        data['capabilities'][name] = capabilities
        path.write_text(json.dumps(data))

    def test_new_skill_does_not_require_preparing_model_evaluations(self):
        result = validate(self.root, full=True)
        self.assertTrue(result['passed'], result['errors'])
        self.assertIn('document-archival', result['capabilities_without_prepared_cases'])

    def test_default_validation_does_not_require_evaluation_or_provenance(self):
        shutil.rmtree(self.root / 'evals')
        shutil.rmtree(self.root / 'provenance')
        result = validate(self.root)
        self.assertTrue(result['passed'], result['errors'])
        self.assertNotIn('prepared_cases', result)
        self.assertNotIn('pinned_files', result)

    def test_claimed_coverage_still_requires_actual_cases(self):
        self.update_case_map('doc-archive', ['document-archival'])
        result = validate(self.root, full=True)
        self.assertFalse(result['passed'])
        self.assertIn('Declared case coverage differs from prepared cases', result['errors'])

    def test_unknown_capability_is_not_accepted_as_optional_coverage(self):
        self.update_case_map('research', ['nonexistent-capability'])
        result = validate(self.root)
        self.assertTrue(result['passed'], result['errors'])
        result = validate(self.root, full=True)
        self.assertFalse(result['passed'])
        self.assertIn('Case capability map has unknown entry or capability: research', result['errors'])

    def test_full_validation_reads_dated_case_fragments(self):
        base = json.loads((self.root / 'evals/cases.json').read_text())
        fragment = {
            'schema_version': 2,
            'capabilities': {},
            'cases': [base['cases'][0]],
        }
        (self.root / 'evals/cases.2099-01-01.json').write_text(json.dumps(fragment))
        result = validate(self.root, full=True)
        self.assertFalse(result['passed'])
        self.assertIn('Duplicate case IDs', result['errors'])

    def test_missing_archive_resource_still_fails(self):
        (self.root / 'skills/doc-archive/references/operations.md').unlink()
        result = validate(self.root)
        self.assertFalse(result['passed'])
        self.assertTrue(any('operations.md' in error for error in result['errors']))

    def append_skill_links(self, text):
        path = self.root / 'skills/skill-dev/SKILL.md'
        path.write_text(path.read_text() + '\n' + text + '\n')

    def test_non_markdown_resources_must_stay_inside_skill(self):
        for filename in ('checker.py', 'config.json', 'image.png'):
            with self.subTest(filename=filename):
                (self.root / filename).write_bytes(b'\x00\xff')
                self.append_skill_links(f'[Required resource](../../{filename})')
                result = validate(self.root)
                self.assertTrue(any('resource escapes standalone folder' in error
                                    and filename in error for error in result['errors']))

    def test_symlink_cannot_hide_external_resource(self):
        outside = self.root / 'checker.py'
        outside.write_text('print(1)\n')
        (self.root / 'skills/skill-dev/checker.py').symlink_to(outside)
        self.append_skill_links('[Required checker](checker.py)')
        result = validate(self.root)
        self.assertFalse(result['passed'])
        self.assertTrue(any('resource escapes standalone folder' in error
                            for error in result['errors']))

    def test_local_binary_and_encoded_paths_are_valid(self):
        (self.root / 'skills/skill-dev/example image.png').write_bytes(b'\x00\xff')
        self.append_skill_links('![Example](example%20image.png)')
        result = validate(self.root)
        self.assertTrue(result['passed'], result['errors'])

    def test_missing_same_file_and_cross_file_anchors_fail(self):
        self.append_skill_links('[Local](#missing-local)\n'
                                '[Remote](references/authoring.md#missing-remote)')
        result = validate(self.root)
        for fragment in ('missing-local', 'missing-remote'):
            self.assertTrue(any('Broken anchor' in error and fragment in error
                                for error in result['errors']))

    def test_heading_and_explicit_anchors_are_valid(self):
        self.append_skill_links('''## Repeat
## Repeat
## Repeat-1
## Repeat
## A `code` & [link](#repeat)
## Padded heading   ###
Setext heading
--------------
<a id="explicit-anchor"></a>
<a name="legacy-anchor"></a>
[First](#repeat)
[Second](#repeat-1)
[Collision](#repeat-1-1)
[Third](#repeat-2)
[Formatting](#a-code--link)
[Padding](#padded-heading)
[Setext](#setext-heading)
[Explicit](#explicit-anchor)
[Legacy](#legacy-anchor)
[Cross-file](references/authoring.md#write-executable-guidance)
''')
        result = validate(self.root)
        self.assertTrue(result['passed'], result['errors'])

    def test_fenced_example_does_not_create_a_heading_anchor(self):
        self.append_skill_links('```markdown\n## Example only\n```\n'
                                '[Missing](#example-only)')
        result = validate(self.root)
        self.assertTrue(any('Broken anchor' in error and 'example-only' in error
                            for error in result['errors']))


if __name__ == '__main__':
    unittest.main()
