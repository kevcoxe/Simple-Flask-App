import sqlite3

from app import DATABASE


def init_db():
    db = sqlite3.connect(DATABASE)
    with open('schema.sql', 'r') as f:
        script = f.read()
        db.executescript(script)

    db.close()


if __name__ == '__main__':
    init_db()

