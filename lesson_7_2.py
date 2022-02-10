# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fabric(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        super().__init__('Пальто')
        self.size = size

    @property
    def fabric(self):
        '''расход ткани'''
        return self.size / 6.5 + 0.5

    def __str__(self):
        return f'{self.name} размера {self.size}, расход ткани {self.fabric:.2f}'



class Suit(Clothes):
    def __init__(self, height):
        super().__init__('Костюм')
        self.height = height

    @property
    def fabric(self):
        '''расход ткани'''
        return 2 * self.height + 0.3

    def __str__(self):
        return f'{self.name} на рост {self.height}, расход ткани {self.fabric:.2f}'

coat1 = Coat(20)
suit1 = Suit(1.74)

print(coat1)
print(suit1)
