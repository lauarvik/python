#«Склад оргтехники»

from abc import ABC, abstractmethod
 
class Office_equip(ABC):
    @abstractmethod
    def __init__(self, price, model, weight, type):
        self.price = price
        self.model = model
        self.weight = weight
        self.type = type
    def __repr__(self):
        return self.model


# Я не вижу уникальных значений для оргтехники.
# С точки зрения склада они все просто коробки с моделью, ценой и весом.
# Чем-то уникальным они становяться уже для конечного потребителя.

class Printer(Office_equip):
    def __init__(self, price, model, weight):
        super().__init__(price, model, weight, 'принтер')


class Scanner(Office_equip):
    def __init__(self, price, model, weight):
        super().__init__(price, model, weight, 'сканер')


class Xerox(Office_equip):
    def __init__(self, price, model, weight):
        super().__init__(price, model, weight, 'МФУ')


class Departament:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Warehouse:
    counter = 1000
    def __init__(self):
        self.db = {}

    def new_equip(self, equip):
        '''Принять оборудование на склад'''
        if not isinstance(equip, (Printer, Scanner, Xerox)):
            print(f'{equip} должен иметь типа {Printer}, {Scanner} или {Xerox}')
            raise TypeError(equip)
        self.__class__.counter += 1
        inv_num = self.__class__.counter
        record = dict(equip=equip, dep=None)
        self.db[inv_num] = record
        return inv_num

    def receive_equip(self, inv_num):
        '''Принять оборудование из подразделения обратно на склад'''
        if not inv_num in self.db:
            raise ValueError(f'Инвентарный номер {inv_num} не существует')
        if not self.db[inv_num]['dep']:
            model = self.db[inv_num]["equip"].model
            raise ValueError(f'Оборудование {inv_num}:{model} уже на складе')
        self.db[inv_num]['dep'] = None
        return True

    def send_equip(self, inv_num, dep):
        '''Отправить оборудование в подразделение'''
        if not inv_num in self.db:
            raise ValueError(f'Инвентарный номер {inv_num} не существует')
        if not isinstance(dep, Departament):
            raise TypeError(f'{dep} должен иметь типа {Departament}')

        if self.db[inv_num]['dep']:
            model = self.db[inv_num]["equip"].model
            dep = self.db[inv_num]["dep"]
            raise ValueError(f'{inv_num}:{model} находится в подразделении {dep}')
        self.db[inv_num]['dep']=dep
        return True

    def using_equip(self):
        '''Оборудование в подразделениях'''
        return dict(filter(lambda i:i[1]['dep'], self.db.items()))

    def available_equip(self):
        '''Доступное оборудование'''
        return dict(filter(lambda i:not i[1]['dep'], self.db.items()))

    def total_cost(self):
        '''Общая стоимость оборудования на складе'''
        from functools import reduce
        def sum_prices(a, b):
            if isinstance(a, dict):
                return a['equip'].price + b['equip'].price
            else:
                return a + b['equip'].price

        return reduce(sum_prices, self.db.values())

#модели оборудования, не экземпляры
#экземляров каждоый модели может быть несколько
printers = [
    Printer(7499, 'Pantum P2502', 4.75),
    Printer(28499, 'HP LaserJet Pro M404dw', 8.56), 
]
scanners = [
    Scanner(25999, 'Canon imageFORMULA DR-F120', 4.6),
    Scanner(26099, 'HP Scanjet Pro 2000 s2', 2.7), 
]
xeroxes = [
    Xerox(15999, 'Brother DCP-1602R', 7.2)
]
deps = [
    Departament('Юридический отдел'),
    Departament('Бухгалтерия'),
    Departament('Отдел кадров'),
    Departament('Отдел продаж'),
]
#список оборудования для приёма на склад
equip_list = [
    printers[1], printers[1], printers[0], 
    scanners[0], scanners[1], 
    xeroxes[0],
]
wh = Warehouse()
print('Получение нового оборудования:')
for i in equip_list:
    inv_n = wh.new_equip(i)
    print(f'Инв. номер: {inv_n}, {i.type}, модель: {i.model}, цена: {i.price}')
try:
    #отправка в подразделение
    wh.send_equip(1001, deps[1])
    wh.send_equip(1002, deps[1])
    wh.send_equip(1003, deps[1])
    wh.send_equip(1004, deps[2])
    wh.send_equip(1006, deps[3])
    print('Оборудование в подразделениях:', wh.using_equip())
    print('Оборудование на складе:', wh.available_equip())
    #возврят на склад
    wh.receive_equip(1001)
    print('Оборудование на складе:', wh.available_equip())
except Exception as e:
    print(e)
print(f'Общая стоимость оборудования на складе {wh.total_cost()}')
