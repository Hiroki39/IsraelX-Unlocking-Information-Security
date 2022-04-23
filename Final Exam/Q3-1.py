# don't change code up to line 40, the database is populated for your own testing

import sqlite3
import os

if os.path.exists('db.sqlite3'):
    os.remove('db.sqlite3')

with sqlite3.connect('db.sqlite3') as connection:
    cursor = connection.cursor()
    cursor.executescript('''
CREATE TABLE notes (
    id INTEGER PRIMARY KEY,
    username TEXT,
    token TEXT,
    text TEXT
);
INSERT INTO notes (username, token, text) VALUES ('alice', 'token-a', 'Reminder: buy milk');
INSERT INTO notes (username, token, text) VALUES ('alice', 'token-a', 'I like Bob');
INSERT INTO notes (username, token, text) VALUES ('bob', 'token-b', 'TODO: write tests');
    ''')

cache = {}   # just a cache to avoid overloading the database


def get_notes(username, token):
    if username in cache:
        return cache[username]
    with sqlite3.connect('db.sqlite3') as connection:
        cursor = connection.cursor()
        cursor.execute('''
            SELECT text
              FROM notes
             WHERE token = '%s'
        ''' % token)
        cache[username] = user_notes = cursor.fetchall()
        return user_notes

# earlier today: get_notes('alice', 'token-a')
# start changing from here!


def hack_alice():
    # return alice's note without using her token
    return get_notes('alice', "' OR username = 'alice' --")
