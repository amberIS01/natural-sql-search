# sql_guard.py
import sqlglot
from sqlglot import expressions as exp

ALLOWED_TABLES = {"departments", "employees", "products", "orders"}

def validate_sql(sql: str) -> str:
    try:
        expr = sqlglot.parse_one(sql, read="postgres")
    except Exception:
        raise ValueError("Invalid SQL syntax")

    # 1) only SELECT
    if expr.key.upper() != "SELECT":
        raise ValueError("Only SELECT queries are allowed")

    # 2) enforce limit
    if not any(isinstance(e, exp.Limit) for e in expr.find_all(exp.Limit)):
        sql = sql.rstrip(";") + " LIMIT 50;"
        expr = sqlglot.parse_one(sql, read="postgres")

    # 3) table allowlist
    for table in expr.find_all(exp.Table):
        if table.name not in ALLOWED_TABLES:
            raise ValueError(f"Disallowed table: {table.name}")

    return expr.sql(dialect="postgres")
