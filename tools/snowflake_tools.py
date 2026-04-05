from auth.snowflake_auth import get_snowflake_connection

def run_query(sql):
    conn = get_snowflake_connection()
    try:
        cur = conn.cursor()
        cur.execute(sql)
        cols = [c[0] for c in cur.description]
        rows = cur.fetchall()
        return {
            "columns": cols,
            "rows": [list(r) for r in rows]
        }
    finally:
        conn.close()