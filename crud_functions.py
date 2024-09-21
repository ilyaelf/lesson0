import sqlite3

connection = sqlite3.connect('Products.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        price INTEGER NOT NULL,
        picture TEXT NOT NULL
    )
    ''')
    connection.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
    )
    ''')
    connection.commit()

def add_product(title, description, price, picture):
    cursor.execute(' INSERT INTO Products (title,description,price,picture) VALUES (?,?,?,?)',
                   (title, description, price, picture))
    connection.commit()


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.commit()
    return products

def add_user(username,email,age,balance):
    cursor.execute('INSERT INTO Users (username,email,age,balance) VALUES (?,?,?,?)',
                   (username,email,age,balance))
    connection.commit()

def is_included(username):
    check_user=cursor.execute("SELECT * FROM Users WHERE username=?",(username,))
    if check_user.fetchone() is None:
        return False
    else:
        return True
    connection.commit()

'''
initiate_db()
add_product('Продукт1', 'Витамин А', 100, 'pic1.png')
add_product('Продукт2', 'Витамин B', 200, 'pic2.png')
add_product('Продукт3', 'Витамин C', 300, 'pic3.png')
add_product('Продукт4', 'Витамин D', 400, 'pic4.png')
'''
