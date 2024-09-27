def custom_write(file_name,strings):
    with open(f'{file_name}',mode='w',encoding='utf-8') as file:
        string_position = {}
        keys = []
        n = 1
        for line in strings:
            p = file.tell()
            keys.append((n,p))
            file.write(line+'\n')
            n+=1
    with open(f'{file_name}',mode='r',encoding='utf-8') as file:
        for i in keys:
            stroka = file.readline().rstrip("\n")
            string_position[i] = stroka
    return string_position

info = ['Text for tell.','Используйте кодировку utf-8.','Because there are 2 languages!','Спасибо!']
result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)