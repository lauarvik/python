#6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

proceeds = float(input("Введите выручку: "))
costs = float(input("Введите издержки: "))

if proceeds >= costs:
    profit = proceeds - costs
    profitability = profit / proceeds
    print(f"Компания отработала с прибылью: {profit}")
    #выведем результат в процентах, если можно
    print(f"Рентабельность: {profitability:.2%}")
    employees = int(input("Введите количество сотрудников: "))
    profit_per_employee = profit / employees
    print(f"Прибыль на одного сотрудника: {profit_per_employee}")
else:
    print(f"Компания отработала с убытками: {proceeds - costs}")
