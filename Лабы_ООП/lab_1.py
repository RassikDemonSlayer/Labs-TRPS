# 3. Создайте класс Rectangle (прямоугольник). 
# Класс имеет атрибуты length (длина) и width (ширина), каждый из которых по умолчанию равен  единице. 
# Он имеет функции-элементы, которые вычисляют периметр (perimeter) и площадь (area) прямоугольника, а также функции записи и чтения как для length, так и для width.
# Функции записи должны проверять, что length и width – числа с плавающей запятой, находящиеся в пределах от 0.0 до 20.0.

class Rectangle:
    def __init__(self):
        self.__length = 1.0
        self.__width = 1.0

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if value>=0 and value<=20:
            self.__length = float(value)
        else:
            print('Длина не валидна, значение осталось по умолчанию')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value>=0 and value<=20:
            self.__width = float(value)
        else:
            print('Ширина не валидна, значение осталось по умолчанию')

    @property
    def perimeter(self):
        return self.length*2 + self.width*2
    
    @property
    def area(self):
        return self.width*self.length
    
rec = Rectangle()
rec.length = 3
rec.width = 3
print(rec.length)
print(rec.width)

print(rec.perimeter)
print(rec.area)