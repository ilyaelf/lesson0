a = int(input("введите число от 3 до 20"))
b = a//2
i = 0
r = ['пароль']
while i < b:
    i = i + 1
    c = a - i
    r = r + list(str(i)) + list(str(c))
    continue
else:
    print(f'{r}')


