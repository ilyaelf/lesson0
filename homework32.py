def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        n = 0
        for i in range(2,int(result**0.5)+1):
            if result%i == 0:
                n +=1
        if n == 0:
            print("простое")
        else:
            print("составное")
        return result
    return wrapper

@is_prime
def sum_three(a,b,c):
    d = a+b+c
    return d

result = sum_three(2,3,6)
print(result)
