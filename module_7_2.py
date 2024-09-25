def custom_write(file_name,strings):
    with open(f'{file_name}',mode='w',encoding='utf-8') as file:
        string_position = {}
        keys = []
        n = 0
        for line in strings:
            p = file.tell()
            keys.append((f'{n},{p}'))
            file.write(line)
            file.write('\n')
            n+=1
    file.close()
    with open(f'{file_name}',mode='r',encoding='utf-8') as file:
        for i in keys:
            stroka = file.readline()
            string_position[i] = stroka
    file.close()
    return string_position

info = ['Text for tell.','Используйте кодировку utf-8.','Because there are 2 languages!','Спасибо!']
result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)