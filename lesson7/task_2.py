from abc import abstractmethod, ABC

class Clothes():
    def __init__(self, name, size, height):
        self.name = name
        self.size = size
        self.height = height

    def __add__(self, other):
        return 2*self.height + 0.3 + other.size/6.5 + 0.5


class Costume(Clothes):

    def consumption(self):
        return 2*self.height + 0.3


class Coat(Clothes):
    def consumption(self):
        return self.size/6.5 + 0.5



a = Costume('Костюм', 50, 180)
print(a.consumption())
m = Coat('Пальто', 50, 180)
print(m.consumption())
print(f'Общий расход ткани {a + m:.3f}')