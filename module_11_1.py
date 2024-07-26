import random
import numpy
import requests
from PIL import Image

print('1. Использование библиотеки numpy\n')
matrix = []
for i in range(1,11):
    line = []
    for j in range(1,11):
        a = random.randint(1,100)
        line.append(a)
    matrix.append(line)
m = numpy.matrix(matrix)
print('матрица из случайных чисел от 1 до 100\n',m)
print('размерность матрицы\n',m.ndim)
print('индексы наибольших эл-тов столбцов\n', m.argmax(0),"\n"'и их значения\n',m.max(0))
print('матрица с отсортированными по возрастанию эл-тами построчно\n',numpy.sort(m,axis=1),"\n")

print('2. Использование библиотеки requests\n')
r = requests.get('https://api.github.com/events', stream=True)
print('вывод http заголовков \n')
for i in r.headers:
    print(f'{i},{r.headers[i]}')
print('вывод потока данных со страницы побитно\n')
print(r.raw.read(100),"\n")
print('отправка кукис на страницу и запрос обратно\n')
jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/cookies')
url = 'https://httpbin.org/cookies'
r = requests.get(url, cookies=jar)
print(r.text,"\n")

print('3. использование библиотеки pillow(PIL)\n')
print('вывод различных свойств изображения\n')
image = Image.open('Vvardenfell_Roadmap.png')
print(image.format, image.size, image.mode, image.info,"\n")
print('изменение размера изображения\n')
image1 =image.resize((900,900),)
image1.show()
print('переворот изображения\n')
image1 = image1.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
image1.show()
print('сохранение изображения в новый файл\n')
image1.save('Vvardenfell_Roadmap1.png')




