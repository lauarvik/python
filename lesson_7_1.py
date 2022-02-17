# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.

class Matrix:
    def __init__(self, data=None):
        self.data = data if data else []

    def __str__(self):
        result = ''
        for y_list in self.data:
            result += ''.join([f'{el:5d}' for el in y_list]) + '\n'
        return result

    @property
    def y(self):
        '''размер матрицы по y'''
        return len(self.data)

    @property
    def x(self):
        '''размер матрицы по x'''
        # т.к. теоретически размеры вложенных списков 
        # могу быть разные, то решим более общую задачу и 
        # найдём размер максимального
        return 0 if not self.data else max([len(i) for i in self.data])
        # если предположить, что размеры одинаковые, то
        # достаточно вернуть размер первого
        #return len(self.data[0])

    def __add__(self, other):
        from itertools import zip_longest
        combined_data = []
        # Математически не имеет смысла складывать матрицы разных порядков,
        # но иногда это может иметь практический смысл.
        # Размер итоговой матрицы должен быть достаточным, чтобы вместить в себя пересечение обеих исходных,
        # несуществующие элементы заполняем нулями
        for list_1, list_2 in zip_longest(self.data, other.data, fillvalue=[0 for _ in range((max(self.x, other.x)))]):
            new_list = list(map(sum, zip_longest(list_1, list_2, fillvalue=0)))
            combined_data.append(new_list)
        return Matrix(combined_data)

    def __iadd__(self, other):
        # Этот метод реализовывать было не обязательно, но интересно.
        # В его отсутствие используется __add__ и создаётся новый объект, что не оптимально.
        # Размеры итоговой матрицы
        x_size = max(self.x, other.x)
        y_size = max(self.y, other.y)
        # увеличиваем размер матрицы, если это необходимо и инициализируем новые ячейки нулями
        if (delta_x := x_size - self.x) > 0:
            for y_list in self.data:
                for _ in range(delta_x):
                    y_list.append(0)
        if (delta_y := y_size - self.y) > 0:
            for _ in range(delta_y):
                self.data.append([0 for _ in range(x_size)])
        # добавляем значения
        for y in range(other.y):
            for x in range(other.x):
                self.data[y][x] += other.data[y][x]
        return self


m_list = [
  Matrix([[31,32],[37,43],[51,86]]),
  Matrix([[3,5,32],[2,4,6],[-1,64,-8]]),
  Matrix([[3,5,8,3],[8,3,7,1]]),
]

m_result = Matrix()
for m in m_list:
    print(f'Матрица {m.x}x{m.y}')
    print(m)
    m_result += m

print(f'Итоговая матрица {m_result.x}x{m_result.y}')
print(m_result)
