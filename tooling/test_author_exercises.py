"""Keep the documented author runner reproducible across retired Skill entries."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from materialize import ROOT


class AuthorExerciseTests(unittest.TestCase):
    def test_runner_preserves_historical_fixture_and_evidence_limits(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / 'run'
            result = subprocess.run(
                [sys.executable, '-B', str(ROOT / 'tooling/run_author_exercises.py'),
                 str(destination)], capture_output=True, text=True, timeout=60)
            self.assertEqual(result.returncode, 0, result.stderr)
            evidence = json.loads((destination / 'results.json').read_text())
            self.assertEqual(evidence['historical_case_ids'], ['prototype-sqlite'])
            self.assertFalse(evidence['independent'])
            self.assertEqual([r['exit_code'] for r in evidence['runs']], [1, 0, 0, 0])
            self.assertTrue(evidence['price_product_unchanged'])
            review = evidence['static_review']
            self.assertFalse(review['subject_executed'])
            self.assertEqual(review['before_hashes'], review['after_hashes'])
            observations = json.loads(
                (destination / 'prototype-sqlite/observations.json').read_text())
            self.assertEqual(len(observations['runs']), 3)
            for run in observations['runs']:
                self.assertEqual(sorted(x['outcome'] for x in run['outcomes']),
                                 ['inserted', 'unique-rejected'])


if __name__ == '__main__':
    unittest.main()
