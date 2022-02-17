# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fabric(self):
        '''расход ткани'''
        pass


class Coat(Clothes):
    fabric_total = 0
    def __init__(self, size):
        super().__init__('Пальто')
        self.__size = size
        self.__class__.fabric_total += self.fabric

    @property
    def fabric(self):
        '''расход ткани'''
        return self.__size / 6.5 + 0.5

    def __str__(self):
        return f'{self.name} размера {self.__size}, расход ткани {self.fabric:.2f}'

    def __repr__(self):
        return f'{self.name}: {self.__size}, {self.fabric:.2f}'




class Suit(Clothes):
    fabric_total = 0
    def __init__(self, height):
        super().__init__('Костюм')
        self.__height = height
        self.__class__.fabric_total += self.fabric

    @property
    def fabric(self):
        '''расход ткани'''
        return 2 * self.__height + 0.3

    def __str__(self):
        return f'{self.name} на рост {self.__height}, расход ткани {self.fabric:.2f}'

    def __repr__(self):
        return f'{self.name}: {self.__height}, {self.fabric:.2f}'


coats = [Coat(20), Coat(25), Coat(22)]
suits = [Suit(1.70), Suit(1.78), Suit(1.72)]

for c in coats + suits:
    print(c)

print(f'Общий расход ткани на все пальто: {Coat.fabric_total:.2f}')
print(f'Общий расход ткани на все костюмы: {Suit.fabric_total:.2f}')
