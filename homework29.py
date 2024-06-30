print("задание 1")
def create_operation(operation):
    if operation == "mul":
        def mul(x,y):
            return x*y
        return mul
    elif operation == "div":
        def div(x,y):
            return x/y
        return div

my_func_mul = create_operation("mul")
print(my_func_mul(12,15))
my_func_div = create_operation("div")
print(my_func_div(30,5))

print("задание 2")

f1 = lambda a,b,c: (a+b)*c
print(f1(2,3,4))

def f2(a,b,c):
    return (a+b)*c
print(f2(2,3,4))

print('задание3')

class Ploschad():
    def __call__(self, a,b):
        return a*b

figure1 = Ploschad()
figure2 = Ploschad()
sides = [2,8]
print(figure1(6,8))
print(figure2(*sides))