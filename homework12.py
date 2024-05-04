def def_test(*a):
    print(a)
    
def factorial(n):
    if n ==1:
        return 1
    else:
        return n * factorial( n - 1)

def_test('1',2,{1,2,3,4},5.5)
n = int(input('введите n:  '))
print(factorial(n))
