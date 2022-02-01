# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

map_dict = dict(One='Один', Two='Два', Three='Три', Four='Четыре', Five='Пять', Six='Шесть', Seven='Семь',
                Eight='Восемь', Nine='Девять', Ten='Десять')
with open('lesson_5_4_eng.txt') as f_in:
    with open('lesson_5_4_rus.txt', 'w', encoding='utf-8') as f_out:
        while 1:
            line = f_in.readline()
            if not line:
                break
            w1, rest = line.split(maxsplit=1)
            #обработку ошибки отсутвующих ключей в словаре, для простоты, опустим
            f_out.write(' '.join([map_dict[w1], rest]))
