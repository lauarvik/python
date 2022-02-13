# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.

class NumericValueError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        class_name = self.value.__class__.__name__
        return f'Ошибка: {class_name}({self.value}) - нечисловое значение'


# При добавлении элементов строкового типа,
# класс автоматически пытается преобразовать их к числовым типам int или float,
# в случае неудачи генерируется ошибка NumericValueError.
class NumericList(list):
    def __init__(self, data=None):
        if data:
            data = list(map(self.str2typed_val, data))
            for value in data:
                if not isinstance(value, (int, float)):
                    raise NumericValueError(value)
            super().__init__(data)
        else:
            super().__init__()

    def __add__(self, other):
        data = list(map(self.str2typed_val, other))
        for value in data:
            if not isinstance(value, (int, float)):
                raise NumericValueError(value)
        return super().__add__(data)

    def __iadd__(self, other):
        data = list(map(self.str2typed_val, other))
        for value in data:
            if not isinstance(value, (int, float)):
                raise NumericValueError(value)
        return super().__iadd__(data)

    def __setitem__(self, key, value):
        value = self.str2typed_val(value)
        if not isinstance(value, (int, float)):
            raise NumericValueError(value)
        super().__setitem__(key, value)

    def append(self, value):
        value = self.str2typed_val(value)
        if not isinstance(value, (int, float)):
            raise NumericValueError(value)
        super().append(value)

    def extend(self, data):
        data = list(map(self.str2typed_val, data))
        for value in data:
            if not isinstance(value, (int, float)):
                raise NumericValueError(value)
        super().extend(data)

    def insert(self, index, value):
        value = self.str2typed_val(value)
        if not isinstance(value, (int, float)):
            raise NumericValueError(value)
        super().insert(index, value)

    @staticmethod
    def str2typed_val(str_val):
        import re
        result = str_val
        if not isinstance(str_val, str):
            return result
        #int
        if re.match('[+-]?\d+$', str_val):
            result = int(str_val)
        #float
        elif re.match('[+-]?\d*\.\d+$', str_val):
            result = float(str_val)
        #float с экспонентой
        elif re.match('[+-]?\d*\.?\d+[eE][+-]?\d+$', str_val):
            result = float(str_val)
        return result


if __name__ == '__main__':
    result_list = NumericList()
    #Пустой ввод - конец программы
    while user_list := input('Введите список чисел, разделенных пробелами: ').split():
        print(f'Исходные данные: {user_list}')
        for val in user_list:
            try:
                result_list.append(val)
            except NumericValueError as e:
                print(e)

        print(f'Итоговый список: {result_list}')
