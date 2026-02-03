import sqlite3

DB_NAME = "bhashasetu.db"

def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)

def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS progress (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        language TEXT,
        count INTEGER DEFAULT 1
    )
    """)

    conn.commit()
    conn.close()

def update_progress(username, language):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT count FROM progress WHERE username = ? AND language = ?",
        (username, language)
    )
    row = cur.fetchone()

    if row:
        cur.execute(
            "UPDATE progress SET count = count + 1 WHERE username = ? AND language = ?",
            (username, language)
        )
    else:
        cur.execute(
            "INSERT INTO progress (username, language, count) VALUES (?, ?, 1)",
            (username, language)
        )

    conn.commit()
    conn.close()


def get_progress(username):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT language, count FROM progress WHERE username = ?",
        (username,)
    )
    data = cur.fetchall()
    conn.close()

    return data
