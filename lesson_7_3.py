# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек.

class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if (result := self.num - other.num) > 0:
            return Cell(result)
        else:
            print(f'Операция вычетания невозможна, результат {result} меньше нуля')

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(self.num // other.num)

    def __str__(self):
        return f'Клетка с {self.num} ячейками'

    def make_order(self, n):
        rows = ['*' * n for _ in range(self.num // n)] + ['*' * (self.num % n)]
        return '\n'.join(rows)


cell_1 = Cell(15)
cell_2 = Cell(20)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

# .encode() добавлено для наглядности, что задание выполнено верно и нет лишних \n
print(cell_1.make_order(6).encode())
print(cell_2.make_order(8).encode())
