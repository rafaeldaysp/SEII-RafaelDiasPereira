import sqlite3
from datetime import datetime

def create_post(name, content):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS posts(id INTEGER PRIMARY KEY AUTOINCREMENT,\
                    name TEXT NOT NULL, content TEXT NOT NULL, ts TEXT)')
    cursor.execute('INSERT INTO posts(name, content, ts) VALUES(?, ?, ?)', (name, content, str(datetime.now())[0:16]))
    connection.commit()
    connection.close()
    
def get_posts():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS posts(id INTEGER PRIMARY KEY AUTOINCREMENT,\
                    name TEXT NOT NULL, content TEXT NOT NULL, ts TEXT)')
    cursor.execute('SELECT * FROM posts')
    return reversed(cursor.fetchall())

def get_post_by_id(id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM posts WHERE id = ' + str(id))
    return cursor.fetchall()

def delete_all_posts():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('DROP TABLE posts')

def delete_post_by_id(id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM posts WHERE id = ' + str(id))
    connection.commit()
    connection.close()
    
def update_post(id, content):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE posts SET content = (?) WHERE ID = ' + str(id), [content])
    cursor.execute('UPDATE posts SET ts = (?) WHERE ID = ' + str(id), [str(datetime.now())[0:16]])
    connection.commit()
    connection.close()

