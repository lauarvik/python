# 5. Реализовать класс Stationery (канцелярская принадлежность).

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'{self.title}: запуск отрисовки')

class Pen(Stationery):
    def __init__(self):
        super().__init__('ручка')

    def draw(self):
        super().draw()
        print('тонкая линия')


class Pencil(Stationery):
    def __init__(self):
        super().__init__('карандаш')

    def draw(self):
        super().draw()
        print('карандашный след')


class Handle(Stationery):
    def __init__(self):
        super().__init__('маркер')

    def draw(self):
        super().draw()
        print('жирная линия')

for s in [Pen(), Pencil(), Handle()]:
    s.draw()
