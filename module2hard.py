a = int(input("введите число от 3 до 20"))
r = ['пароль']
for i in range(1,20):
    for j in range(1,20):
        if a == i+j and i < j:
            r = r + [f'{i}{j}']
        else:
            if a % (i+j) == 0 and i != j and i < j:
                r = r + [f'{i}{j}']

print(f'{r}')


