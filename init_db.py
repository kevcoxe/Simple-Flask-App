import sqlite3

from app import DATABASE


def init_db():
    db = sqlite3.connect(DATABASE)
    with open('schema.sql', 'r') as f:
        script = f.read().decode('utf8')
        db.executescript(script)

    db.close()
