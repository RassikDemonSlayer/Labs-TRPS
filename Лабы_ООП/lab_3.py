# 3. Создать класс-родитель точка, 
# его наследника - класс отрезок, 
# наследников отрезка «квадрат», «параллелограмм» (нарисовать, стереть, закрасить, передвинуть, повернуть).

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
        

class Vector(Point):
    def __init__(self):
        pass
    
class Square(Vector):
    pass

class Parallelogram(Vector):
    pass


        
