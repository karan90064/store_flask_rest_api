import sqlite3

# create  conn
connection = sqlite3.connect('data.db')

# cursor to execute queries
cursor = connection.cursor()

create_table = "create table users (id int, username text, password text)"

insert_user = "insert into users values (?, ?, ?)"

select_users = "select * from users"

select_items = "select * from items"

user_1 = (1, 'karan', 'krn')

users = [
    (2, 'rakesh', 'rks'),
    (3, 'siddh', 'sid')
]


# cursor.execute(create_table)
# connection.commit()
#
#
# cursor.execute(insert_user, user_1)
# connection.commit()
#
# cursor.executemany(insert_user, users)
# connection.commit()

print( type(cursor.execute(select_users)))

print("rows in users")
for row in cursor.execute(select_users):
    print(row)

print("rows in items")
for row in cursor.execute(select_items):
    print(row)

connection.close()


