import sqlite3

with sqlite3.connect('db.sqlite3') as connection:
    cursor = connection.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    cursor.execute('INSERT OR IGNORE INTO users VALUES (1, "alice", "1234")')
    cursor.execute('INSERT OR IGNORE INTO users VALUES (2, "bob", "5678")')


def authenticate(username, password):
    with sqlite3.connect('db.sqlite3') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = :username AND password = :password",
                       {'username': username, 'password': password})  # change this line only
        return len(cursor.fetchall()) > 0
