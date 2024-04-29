def print_params(a = 1.2, b = 10, c = 'True'):
    print(a, b ,c)

print_params(6,7,8)
print_params(6,9)
print_params(b=25)
print_params(c=[1,2,3])

values_list = [5.5, 10,"zzz"]
values_dict = {'a':4.9,'b':100500,'c':"aaa"}

print_params(*values_list)
print_params(**values_dict)

values_list2 = [values_list,values_dict]

print_params(*values_list2, 42)