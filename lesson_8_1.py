# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).

class Date:
    def __init__(self, strdate):
        self.strdate = strdate
        self.day = self.month = self.year = 0
        self.is_valid = False
        try:
            self.day, self.month, self.year = self.__class__.to_nums(strdate)
            if self.__class__.validate(self.day, self.month, self.year):
                self.is_valid = True
                #print(f'Valid date: {strdate}')
            else:
                pass
                #print(f'Invilid date value: {strdate}')
        except:
            pass
            #print(f'Invilid date format: {strdate}')

    @classmethod
    def to_nums(cls, strdate):
        import re
        if m := re.match('(\d{1,2})-(\d{1,2})-(\d{4})$', strdate):
            day, month, year = m.groups()
            return int(day), int(month), int(year)

    @staticmethod
    def validate(day, month, year):
        valid_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # каждый 4й год - високосный, каждый 100й - нет, а каждый 400й - опять да
        valid_days[2] = 28 if year % 4 or not year % 100 and year % 400 else 29
        if month in range(1, 13) and day in range(1, valid_days[month] + 1) and year in range(0, 10000):
           return True

    def __str__(self):
        status = '' if self.is_valid else ' (invalid)'
        return f'{self.strdate}{status}'

    def __repr__(self):
        status = '' if self.is_valid else ' (invalid)'
        return f'{self.strdate}{status}'


dates = [Date('11-12-2007'), Date('29-02-1900'), Date('01-13-1984'), Date('01.01.1984'), Date('01-xx-1984')]
for d in dates:
    print(d)
