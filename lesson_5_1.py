# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

with open('lesson_5_1.txt', 'w', encoding='utf-8') as f:
    while 1:
        input_line = input('Введите строку: ')
        if not input_line:
            break
        print(input_line, file=f)
