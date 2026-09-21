#!/usr/bin/env python3
"""Reproduce transparent author exercises; not an isolated agent evaluation."""
import argparse
import hashlib
import json
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from materialize import ROOT, materialize

CART_TEST = '''import unittest
from cart import add_item

class CartTests(unittest.TestCase):
    def test_independent_users(self):
        first = add_item("apple")
        second = add_item("pear")
        self.assertEqual(first, ["apple"])
        self.assertEqual(second, ["pear"])
        self.assertIsNot(first, second)

    def test_explicit_cart_is_preserved(self):
        cart = ["existing"]
        self.assertIs(add_item("new", cart), cart)
        self.assertEqual(cart, ["existing", "new"])

    def test_explicit_empty_cart_is_preserved(self):
        cart = []
        self.assertIs(add_item("new", cart), cart)
        self.assertEqual(cart, ["new"])
'''
CART_FIX = '''def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart
'''
PRICE_TEST = '''import unittest
from price import total

class PriceTests(unittest.TestCase):
    def test_worked_examples(self):
        for unit_price, quantity, expected in [(125, 3, 375), (125, 0, 0), (0, 9, 0), (7, 1, 7)]:
            with self.subTest(unit_price=unit_price, quantity=quantity):
                self.assertEqual(total(unit_price, quantity), expected)
'''
SQLITE_EXPERIMENT = '''import concurrent.futures
import json
import sqlite3
import tempfile
import threading
from pathlib import Path

results = []
for run in range(3):
    with tempfile.TemporaryDirectory() as directory:
        database = str(Path(directory) / "experiment.sqlite")
        with sqlite3.connect(database) as db:
            db.execute("CREATE TABLE requests (tenant_id TEXT NOT NULL, request_id TEXT NOT NULL, UNIQUE(tenant_id, request_id))")
        start = threading.Barrier(2)
        def insert_one(worker):
            db = sqlite3.connect(database, timeout=5)
            try:
                start.wait(timeout=5)
                db.execute("INSERT INTO requests VALUES (?, ?)", ("tenant-a", "request-1"))
                db.commit()
                return {"worker":worker, "outcome":"inserted"}
            except sqlite3.IntegrityError as error:
                db.rollback()
                return {"worker":worker, "outcome":"unique-rejected", "error":str(error)}
            finally:
                db.close()
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            outcomes = list(pool.map(insert_one, [1, 2]))
        assert sorted(x["outcome"] for x in outcomes) == ["inserted", "unique-rejected"], outcomes
        with sqlite3.connect(database) as db:
            same_tenant = db.execute("SELECT COUNT(*) FROM requests WHERE tenant_id=?", ("tenant-a",)).fetchone()[0]
            assert same_tenant == 1, same_tenant
            db.execute("INSERT INTO requests VALUES (?, ?)", ("tenant-b", "request-1"))
            db.commit()
            rows = db.execute("SELECT tenant_id, request_id FROM requests ORDER BY tenant_id").fetchall()
            assert rows == [("tenant-a", "request-1"), ("tenant-b", "request-1")], rows
        results.append({"run":run + 1, "outcomes":outcomes, "rows":rows})
print(json.dumps({"sqlite_version":sqlite3.sqlite_version, "journal_mode":"default DELETE", "runs":results,
    "limit":"Local SQLite, three simultaneous-start schedules. No claim about all interleavings, process crashes, other database engines, or production settings."}, indent=2))
'''


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination', type=Path, help='A new directory, never an existing run')
    args = parser.parse_args()
    destination = args.destination.resolve()
    if destination.exists():
        parser.error('Destination exists; preserve old evidence and choose a new directory')
    destination.mkdir(parents=True)
    cases = {c['id']:c for c in json.loads((ROOT/'evals/cases.json').read_text())['cases']}
    def prepare(case_id):
        materialize(cases[case_id], destination/case_id)
        return destination/case_id/'workspace'
    runs = []
    def run(case_id, workspace, args, log_name):
        result = subprocess.run([sys.executable, *args],cwd=workspace,text=True,capture_output=True)
        log = '$ python3 ' + ' '.join(args) + '\n' + result.stdout + result.stderr
        log += '\nexit_code=' + str(result.returncode) + '\n'
        (workspace.parent/log_name).write_text(log)
        runs.append({'case':case_id,'command':['python3',*args],'cwd':str(workspace.relative_to(destination)),
                     'exit_code':result.returncode,'log':str((workspace.parent/log_name).relative_to(destination))})
        return result

    cart = prepare('debug-wrong-theory')
    original = (cart/'cart.py').read_text()
    (cart.parent/'cart.before.py').write_text(original)
    (cart/'test_cart.py').write_text(CART_TEST)
    red = run('debug-wrong-theory',cart,['-B','-m','unittest','-v','test_cart'],'red.log')
    assert red.returncode == 1 and 'test_independent_users' in red.stderr and 'FAIL:' in red.stderr, red
    (cart/'cart.py').write_text(CART_FIX)
    green = run('debug-wrong-theory',cart,['-B','-m','unittest','-v','test_cart'],'green.log')
    assert green.returncode == 0, green
    (cart.parent/'reasoning.md').write_text(
        '# Author exercise: shared default state\n\n'
        'Two calls without an explicit cart reuse the default list. The second append also changes the first caller’s returned list; the behavioral red run shows this. '
        'There is no encoding transformation in this path. Allocating only when cart is None fixes implicit-call isolation and preserves the identity of an explicitly supplied cart, including an empty one. '
        'The green run covers these three cases. This is a narrow fixture observation, not an independent evaluation of the debug Skill.\n')

    price = prepare('implement-test-code')
    price_before = digest(price/'price.py')
    (price/'test_price.py').write_text(PRICE_TEST)
    price_run = run('implement-test-code',price,['-B','-m','unittest','-v','test_price'],'tests.log')
    assert price_run.returncode == 0
    assert digest(price/'price.py') == price_before

    sqlite = prepare('prototype-sqlite')
    (sqlite/'experiment.py').write_text(SQLITE_EXPERIMENT)
    sqlite_run = run('prototype-sqlite',sqlite,['-B','experiment.py'],'experiment.log')
    assert sqlite_run.returncode == 0, sqlite_run.stderr
    (sqlite.parent/'observations.json').write_text(sqlite_run.stdout)

    review = prepare('review-code-regression')
    before = {name:digest(review/name) for name in cases['review-code-regression']['files']}
    # Read the exact snapshots. Do not import or run the subject of this static-only case.
    original = (review/'old.py').read_text()
    changed = (review/'new.py').read_text()
    contract = (review/'contract.md').read_text()
    assert 'except TimeoutError:' in original and 'except' not in changed and 'unavailable' in contract
    (review.parent/'review.md').write_text(
        '# Author static review\n\n'
        '**[P1] Preserve the timeout fallback — workspace/new.py:2.** '
        'When fetch() raises TimeoutError, the new implementation propagates it to the display caller. '
        'The old snapshot catches this exception and returns unavailable; contract.md explicitly requires that result. '
        'Restore the timeout handling (or a verified equivalent at this boundary) while preserving the normal return.\n\n'
        'Scope: both complete snapshots and the supplied behavior contract. No tests or subject code were run; files were not changed. '
        'This is an author exercise with known grading criteria, not independent review or runtime acceptance.\n')
    after = {name:digest(review/name) for name in before}
    assert before == after
    evidence = {
        'kind':'author-exercises','independent':False,'blind':False,'baseline_comparison':False,
        'time_utc':datetime.now(timezone.utc).isoformat(),'python':platform.python_version(),
        'case_ids':['debug-wrong-theory','implement-test-code','prototype-sqlite','review-code-regression'],
        'runs':runs, 'static_review':{'subject_executed':False,'before_hashes':before,'after_hashes':after},
        'price_product_unchanged':digest(price/'price.py')==price_before,
        'limits':'Author knows both methods and criteria. Mechanistic local observations only; not a measure of triggering, independent execution quality, or improvement over upstream/default harness.'
    }
    (destination/'results.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(evidence,ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
