
with open('homework23.txt',mode = 'r', encoding='utf8') as poem:
    for line in poem:
        print(line,end = '')
    print('')
    print(poem.closed)
print(poem.closed)
#в отступе файл еще открыт, а далее, на втором принте он закрыт



