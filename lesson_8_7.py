# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. 
# Складывать и вычитать комплексные числа можно с помощью правила: (a + bi) ± (c + di) = (a ± c) + (b ± d)i.
# Умножение комплексных чисел выполняют таким образом: (a + bi) · (c + di) = (ac – bd) + (ad + bc)i.

class MyComplex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, (MyComplex, complex)):
            return MyComplex(self.real + other.real, self.imag + other.imag)
        elif isinstance(other, (int, float)):
            return MyComplex(self.real + other, self.imag)
        else:
            raise TypeError(other)

    def __mul__(self, other):
        if isinstance(other, (MyComplex, complex)):
            return MyComplex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)
        elif isinstance(other, (int, float)):
            return MyComplex(self.real * other, self.imag * other)
        else:
            raise TypeError(other)

    def __str__(self):
        return f'{self.real}+{self.imag}i'


if __name__ == '__main__':
    my_c1 = MyComplex(2, 1)
    my_c2 = MyComplex(3, 4)
    c1 = 2+1j
    c2 = 3+4j
    print(my_c1, '+', my_c2, '=', my_c1 + my_c2)
    print('Проверка:', c1 + c2)
    print(my_c1, '*', my_c2, '=', my_c1 * my_c2)
    print('Проверка:', c1 * c2)
    print(my_c1, '*', 2, '=', my_c1 * 2)
    print('Проверка:', c1 * 2)
    print(my_c2, '+', 2, '=', my_c2 + 2)
    print('Проверка:', c2 + 2)
