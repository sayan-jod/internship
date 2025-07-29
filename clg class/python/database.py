import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

#craete table
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')

cursor.execute('INSERT INTO users (name) VALUES ("sayan")')
conn.commit()

cursor.execute('SELECT * FROM users')
print(cursor.fetchall())

conn.close()
