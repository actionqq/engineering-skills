import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from materialize import ROOT, materialize


class MaterializerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.dest = Path(self.temp.name) / 'case'
        self.case = {'request':'raw request','setup':'Python available',
                     'files':{'main.py':'print(1)\n'}, 'expect':['SECRET_ORACLE'],
                     'reject':['SECRET_GRADING'], 'skill':'hidden-label'}

    def test_grading_answers_are_not_exported(self):
        materialize(self.case, self.dest)
        files = sorted(str(p.relative_to(self.dest)) for p in self.dest.rglob('*') if p.is_file())
        self.assertEqual(files, ['request.md','workspace/main.py'])
        text = ''.join(p.read_text() for p in self.dest.rglob('*') if p.is_file())
        for hidden in ['SECRET_ORACLE','SECRET_GRADING','hidden-label']:
            self.assertNotIn(hidden,text)

    def test_refuses_overwriting_user_state(self):
        self.dest.mkdir()
        (self.dest / 'mine.txt').write_text('keep')
        with self.assertRaises(FileExistsError):
            materialize(self.case, self.dest)
        self.assertEqual((self.dest / 'mine.txt').read_text(),'keep')

    def test_refuses_path_escape_before_writing(self):
        for invalid in ['.','../outside','/tmp/outside','x/../../outside','x\\..\\outside']:
            with self.subTest(invalid=invalid):
                self.case['files']={invalid:'x'}
                with self.assertRaises(ValueError):
                    materialize(self.case,self.dest)
                self.assertFalse(self.dest.exists())

    def test_wip_contains_index_worktree_and_untracked(self):
        cases=json.loads((ROOT/'evals/cases.json').read_text())['cases']
        case=next(c for c in cases if c['id']=='review-mixed-wip')
        materialize(case,self.dest)
        cwd=self.dest/'workspace'
        def git(*args):
            return subprocess.check_output(['git',*args],cwd=cwd,text=True)
        status=git('status','--porcelain')
        self.assertIn('MM tracked.py',status)
        self.assertIn('?? untracked.py',status)
        self.assertIn('return 1',git('show','HEAD:tracked.py'))
        self.assertIn('return 2',git('show',':tracked.py'))
        self.assertIn('return 3',(cwd/'tracked.py').read_text())


if __name__=='__main__':
    unittest.main()
