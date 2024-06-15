a = int(input('введите а:'))
b = int(input('введите b:'))
class MyExceptionA(Exception):
    global a
    if a > 100:
        print('ошибка: значение а>100')

class MyExceptionB(Exception):
    global b
    if b < 5:
        print('ошибка: значение b<5')

def f(a,b):
    return a+b

try:
    print(f(a,b))
except MyExceptionB:
    raise
except MyExceptionA:
    raise
