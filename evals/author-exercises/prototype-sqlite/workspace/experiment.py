import concurrent.futures
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
