# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open('lesson_5_2.txt', encoding='utf-8') as f:
    lc = wc_total = 0
    for line in f:
        lc += 1
        wc = len(line.split())
        wc_total += wc
        print(f'{line}Строка: {lc}, слов в строке: {wc}')
print(f'Всего в файле {f.name} строк: {lc}, слов {wc_total}')
