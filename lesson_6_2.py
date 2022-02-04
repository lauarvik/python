# Реализовать класс Road (дорога).
class Road:
   def __init__(self, length, width):
       self._length = length #м
       self._width = width #м
       self.thickness = 5 #см
       self.weight_1m2 = 25 #кг

   def get_weight(self):
       #результат в тоннах, поэтому делим на 1000
       return self._length * self._width * self.thickness * self.weight_1m2 / 1000

roads = {
    Road(5000, 20),
    Road(7000, 15),
    Road(15000, 25),
}

for r in roads:
    print(r.get_weight())
