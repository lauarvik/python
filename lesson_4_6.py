# 6. Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее. 

from itertools import count, cycle

my_list = [17, 32, 'boo', None]

for i in count(3):
    print(i, end=' ')
    if i >= 10: 
        print()
        break

count = 10
for i in cycle(my_list):
    if not count:
        print()
        break
    print(i, end=' ')
    count -= 1
