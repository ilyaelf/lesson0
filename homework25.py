import os
import time

directory = 'D:\PYPrFoUn\pythonProject1\domashka'

for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = os.path.join(root, file)
    filetime = os.path.getmtime(filepath)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(filepath)
    parent_dir = os.path.dirname(filepath)
    print(f'Обнаружен файл: {file:50}, Путь: {filepath:100}, Размер: {filesize:12} байт, '
          f'Время изменения: {formatted_time:20}, Родительская директория: {parent_dir:100}')