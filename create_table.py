import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# to make autoincrement   id int - id INTEGER
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

# to make items table
create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_table)

cursor.execute("insert into items values (NULL, 'test', 10.29)")


connection.commit()

connection.close()