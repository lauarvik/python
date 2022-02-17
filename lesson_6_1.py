# 1. Создать класс TrafficLight (светофор).

class TrafficLight:
    states = dict(red=7, yellow=2, green=5)
    __color = None
    def running(self):
        from itertools import cycle
        from time import sleep
        for self.__color, delay in cycle(self.states.items()):
            print(f'{self.__color:6s} - ждём {delay} сек.')
            sleep(delay)
            yield self.__color

tl = TrafficLight()
for color in tl.running():
    pass
