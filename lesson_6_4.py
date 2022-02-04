# 4. Реализуйте базовый класс Car.

import random

class Car:
    def __init__(self, color, name, is_police=False):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police 

    def go(self, speed):
        self.speed += speed
        print(f'{self.name}: газуй!')
        self.show_speed()

    def stop(self):
        self.speed = 0
        print(f'{self.name}: тормози, тормози!')
        self.show_speed()

    def turn(self, direction):
        print(f'{self.name}: поворочиваем {direction}')

    def show_speed(self):
        print(f'{self.name}: текущая скорость {self.speed}')

class TownCar(Car):
    speed_limit = 60
    def show_speed(self):
        super().show_speed()
        if self.speed > self.speed_limit:
            print(f'{self.name}: Превышение скорости!')

class SportCar(Car):
    pass

class WorkCar(Car):
    speed_limit = 40
    def show_speed(self):
        super().show_speed()
        if self.speed > self.speed_limit:
            print('Превышение скорости!')

class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, True)


cars = {
    SportCar('красный', 'LADA VESTA SPORT'),
    WorkCar('белый', 'Газель'),
    TownCar('красный', 'LADA VESTA Седан'),
    PoliceCar('белый', 'УАЗ Патриот'),
}

for c in cars:
    for _ in range(3):
        c.go(random.randint(15, 40))
        c.turn(random.choice(('налево', 'направо')))
    c.stop()
    print('-' * 24)
