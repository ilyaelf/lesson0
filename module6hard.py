class Figure():
    sides_count = 0
    __sides = []
    __color = []
    filled = True

    def __init__(self, color, *sides):
        if self.__is_valid_color(color):
            self.__color = color
        else:
            self.__color = (0, 0, 0)
        self.__sides = sides
        Figure.sides_count = len(self.__sides)

    def get_color(self):
        res = self.__color
        return res

    def __is_valid_color(self, color):
        a = True
        for i in color:
            if i<0 or i>255:
                a = False
        return a

    def set_color(self, color):
        if self.__is_valid_color(color):
            self.__color = color

    def __is_valid_sides(self, sides):
        a = 1
        for i in sides:
            if i>0 and isinstance(i, int):
                pass
            else:
                a = 0
        if len(sides) == self.sides_count and a:
            return True
        else:
            return False

    def get_sides(self):
        res = self.__sides
        return res

    def __len__(self):
        res = 0
        for i in self.__sides:
            res += i
        return res

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = new_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        if len(sides) == self.sides_count:
            self.__sides = sides
        else:
            self.__sides = [1]
        if self.__is_valid_color(color):
            self.__color = color
        else:
            self.__color = (0, 0, 0)

    def get_square(self):
        self.__radius = self.__sides[0] / (2 * 3.14)
        res = 3.14 * self.__radius ** 2
        return res

    def get_color(self):
        res = self.__color
        return res

    def get_sides(self):
        res = self.__sides
        return res

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = new_sides
    def __is_valid_color(self, color):
        a = True
        for i in color:
            if i<0 or i>255:
                a = False
        return a

    def __is_valid_sides(self, sides):
        a = 1
        for i in sides:
            if i>0 and isinstance(i, int):
                pass
            else:
                a = 0
        if len(sides) == self.sides_count and a:
            return True
        else:
            return False

    def __len__(self):
        res = 0
        for i in self.__sides:
            res += i
        return res
class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        if len(sides) == self.sides_count:
            self.__sides = sides
        else:
            self.__sides = [1,1,1]
        if self.__is_valid_color(color):
            self.__color = color
        else:
            self.__color = (0, 0, 0)

    def get_color(self):
        res = self.__color
        return res

    def __is_valid_color(self, color):
        a = True
        for i in color:
            if i<0 or i>255:
                a = False
        return a

    def set_color(self, color):
        if self.__is_valid_color(color):
            self.__color = color

    def __is_valid_sides(self, sides):
        a = 1
        for i in sides:
            if i>0 and isinstance(i, int):
                pass
            else:
                a = 0
        if len(sides) == self.sides_count and a:
            return True
        else:
            return False

    def get_sides(self):
        res = self.__sides
        return res

    def __len__(self):
        res = 0
        for i in self.__sides:
            res += i
        return res

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = new_sides

    def get_square(self):
        s=0
        for i in self.__sides:
            s +=i
        p=s/2
        res = (p*(p-self.__sides[0])*(p-self.__sides[1])*(p-self.__sides[2]))**0.5
        return res

class Cube(Figure):
    sides_count = 12
    __sides = []
    def __init__(self, color, *sides):
        if len(sides) == 1:
            for i in range(12):
                self.__sides.append(sides[0])
        else:
            for i in range(12):
                self.__sides.append(1)
        if self.__is_valid_color(color):
            self.__color = color
        else:
            self.__color = (0, 0, 0)
    def get_color(self):
        res = self.__color
        return res

    def __is_valid_color(self, color):
        a = True
        for i in color:
            if i<0 or i>255:
                a = False
        return a

    def set_color(self, color):
        if self.__is_valid_color(color):
            self.__color = color

    def __is_valid_sides(self, sides):
        if len(sides) == 1:
            if isinstance(sides[0],int) and sides[0] > 0:
                 return True
            else:return False
        else:
            return False

    def get_sides(self):

        return self.__sides

    def __len__(self):
        res = 0
        for i in self.__sides:
            res += i
        return res

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = []
            for i in range(12):
                self.__sides.append(new_sides[0])

    def get_volume(self):
        return self.__sides[0]**3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color((55, 66, 77)) # Изменится
print(circle1.get_color())
cube1.set_color((300, 70, 15)) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())