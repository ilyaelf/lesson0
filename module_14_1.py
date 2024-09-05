import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')
connection.commit()

for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username,email,age,balance) VALUES (?,?,?,?)',
                   (f'User{i}', f'example{i}@gmail.com', f'{10 * i}', f'1000'))
connection.commit()
for i in range(1, 11):
    if i % 2 != 0:
        cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (500, f'User{i}'))
connection.commit()
n = 1
while n<=10:
    cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{n}',))
    n = n + 3
    connection.commit()

cursor.execute("SELECT username,email,age,balance FROM Users WHERE age != 60")
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]}| Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')
connection.commit()
connection.close()
