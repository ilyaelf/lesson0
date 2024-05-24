def data_structure_sum(*args):
    n = []
    def spisok(a):#делает списки из этого винегрета
        if isinstance(a, list):
            for i in range(len(a)):
                if isinstance(a[i], str):
                    a[i] = len(a[i])
                else:
                    if isinstance(a[i], dict):
                        a[i] = list(dict.items(a[i]))
                        spisok(a[i])
                    else:
                        if isinstance(a[i], (set, tuple, list)):
                            a[i] = list(a[i])
                            spisok(a[i])
                        else:
                            spisok(a[i])
    def summa(a):#складывает списки и делает один из чисел суммы вложенных списков
        for i in range(len(a)):
            if isinstance(a[i], int):
                n.append(a[i])
            else:
                summa(a[i])
    spisok(data_structure)#причесываем
    summa(data_structure)#собираем в список из int
    result = sum(n)#складываем
    return result#возвращаем


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = (data_structure_sum(data_structure))
print(result)#две недели мучался, разбирался. когда пошли лекции по классам, начал лучше понимать про глобальные переменные и порядок исполнения и таки сделал!!!!