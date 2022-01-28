# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить результат вычисления произведения всех элементов списка.
from functools import reduce

my_list = [x for x in range(100, 1001) if not x % 2]
result = reduce(lambda x,y: x*y, my_list)
print(result)
