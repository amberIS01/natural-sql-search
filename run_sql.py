# run_sql.py
import os
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

def run_sql(sql: str):
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            # enforce read-only + timeout
            cur.execute("SET LOCAL statement_timeout = '5000';")
            cur.execute("SET LOCAL transaction_read_only = on;")

            cur.execute(sql)
            rows = cur.fetchall()

            return [dict(r) for r in rows]
