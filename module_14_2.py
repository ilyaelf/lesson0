import sqlite3

connection = sqlite3.connect('not_telegram1.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username,email,age,balance) VALUES (?,?,?,?)',
                   (f'User{i}', f'example{i}@gmail.com', f'{10 * i}', f'1000'))

for i in range(1, 11):
    if i % 2 != 0:
        cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (500, f'User{i}'))
connection.commit()
n = 1
while n<=10:
    cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{n}',))
    n = n + 3
connection.commit()

cursor.execute("DELETE FROM Users WHERE id = 6")                # Удаление пользователя с id=6
connection.commit()

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]                              # Подсчёт кол-ва всех пользователей
cursor.execute("SELECT SUM(balance) FROM Users")
sum_balances = cursor.fetchone()[0]                             # Подсчёт суммы всех балансов
print(sum_balances/total_users)

connection.commit()
connection.close()
