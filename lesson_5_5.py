#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

from random import randint
from functools import reduce

with open('lesson_5_5.txt', 'w') as f:
    f.write(' '.join([str(randint(0, 1000)) for x in range(0, 1000)]))

with open('lesson_5_5.txt') as f:
    my_list = f.read().split()

result = reduce(lambda x,y: int(x)+int(y), my_list)
print(f'Сумма чисел в файле: {result}')
