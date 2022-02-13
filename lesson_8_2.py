# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyDivZeroError(Exception):
    def __init__(self, msg):
        self.message = msg


try:
   a, b = input('Введите делимое и делитель (через пробел): ').split()
   a = int(a)
   b = int(b)
   if not b:
       raise MyDivZeroError(f'Ошибка деления на ноль: {a}/{b}')
   result = a / b
   print(f'{a} / {b} = {result}')

except Exception as e:
    excption_class_name = e.__class__.__name__
    print(f'{excption_class_name}: {e}')

except MyDivZeroError as e:
    print(e)
