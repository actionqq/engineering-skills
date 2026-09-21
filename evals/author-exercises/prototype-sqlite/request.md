用 Python 标准库对本机 SQLite 做可重复实验：两条独立连接同时插入相同 tenant_id/request_id，唯一约束应只留下一个记录；再确认不同租户可使用同一 request_id。保存实际结果。

环境说明：允许临时数据库和本地线程；实验对象就是本机 SQLite，不代表其他数据库。

工作目录：workspace/
