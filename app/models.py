import sqlite3
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row
    return g.db

def init_db():
    db = get_db()
    db.executescript('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY, name TEXT, email TEXT
    );
    CREATE TABLE IF NOT EXISTS emails (
        id INTEGER PRIMARY KEY, user_id INTEGER, sent_at TEXT, clicked_at TEXT, submitted_at TEXT
    );
    ''')
    db.commit()
