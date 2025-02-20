# 3. Создайте класс box, конструктору которого передаются три величины типа double, представляющие длины сторон параллелепипеда. 
# Класс box должен подсчитывать его объем и хранить результат типа double. 
# Включите функцию-член voi(), которая выводит на экран объем каждого объекта класса box.

import numpy as np

class Box:
    volumes = []
    def __init__(self, x, y, z):
        self.x = np.float64(x)
        self.y = np.float64(y)
        self.z = np.float64(z)
        self.volume = (self.x * self.y * self.z)
        Box.volumes.append(self.volume)
    
    @classmethod
    def voi(cls):
        return cls.volumes
        
b1 = Box(2.343, 0.000000000000000000000000112123515, 4.0125)
print(b1.x)
print(b1.y)
print(b1.z)

b2 = Box(1.00, 2.04, 35.53)
print(b2.volume)
print(Box.voi())