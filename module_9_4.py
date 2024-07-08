import random

first = 'Мама мыла раму'
second = 'Рамена мало было'
sravnenie = list(map(lambda x,y: x == y,first,second))
print(sravnenie)

def get_advanced_writer(file_name):
    def write_everything(*args):
        with open(file_name,mode='w+',encoding='utf8') as file:
            data = args
            for line in data:
                line = str(line)
                file.write(line)
                file.write("\n")
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
    def __init__(self,*args):
        self.words = list(args)
    def __call__(self, *args, **kwargs):
        result = random.choice(self.words)
        return result

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())