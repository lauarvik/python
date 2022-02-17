# 3. Реализовать базовый класс Worker (работник).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = dict(wage=wage, bonus=bonus)

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

employees = {
    Position('Сафия', 'Виноградова', 'уборщица', 20000, 5000),
    Position('Амина', 'Виноградова', 'продавец', 25000, 5000),
    Position('Егор', 'Егоров', 'грузчик', 27000, 6000),
}

for emp in employees:
    print(f'Работкик: {emp.get_full_name()}, должность: {emp.position}, доход {emp.get_total_income()}')
