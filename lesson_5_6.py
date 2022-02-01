# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.

import re

def conv2int(s):
    m = re.match('\d+', s)
    return int(m[0]) if m else 0 


disciplines = {}
with open('lesson_5_6.txt', encoding='utf-8') as f:
    while 1:
        line = f.readline()
        if not line:
            break
        name, lec, pr, lab = line.split()
        summ = conv2int(lec) + conv2int(pr) + conv2int(lab)
        disciplines[name.strip(':')] = summ

print(disciplines)
