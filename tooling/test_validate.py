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
        result = validate(self.root)
        self.assertTrue(result['passed'], result['errors'])
        self.assertIn('document-archival', result['capabilities_without_prepared_cases'])

    def test_claimed_coverage_still_requires_actual_cases(self):
        self.update_case_map('doc-archive', ['document-archival'])
        result = validate(self.root)
        self.assertFalse(result['passed'])
        self.assertIn('Declared case coverage differs from prepared cases', result['errors'])

    def test_unknown_capability_is_not_accepted_as_optional_coverage(self):
        self.update_case_map('research', ['nonexistent-capability'])
        result = validate(self.root)
        self.assertFalse(result['passed'])
        self.assertIn('Case capability map has unknown entry or capability: research', result['errors'])

    def test_missing_archive_resource_still_fails(self):
        (self.root / 'skills/doc-archive/references/operations.md').unlink()
        result = validate(self.root)
        self.assertFalse(result['passed'])
        self.assertTrue(any('operations.md' in error for error in result['errors']))


if __name__ == '__main__':
    unittest.main()
