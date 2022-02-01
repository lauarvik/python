#3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.

employees = []
with open('lesson_5_3.txt', encoding='utf-8') as f:
    while 1:
        line = f.readline()
        if not line:
            break
        employee = {}
        employee['name'], salary = line.split()
        employee['salary'] = float(salary)
        employees.append(employee)

#Определить, кто из сотрудников имеет оклад менее 20 тысяч
less20k_employees = [x['name'] for x in employees if x['salary'] < 20000]
print(f'Фамилии сотрудников, имеющих оклад меньше 20000: {less20k_employees}')

#подсчёт средней величины дохода сотрудников.
average_salary = sum([x['salary'] for x in employees]) / len(employees)
print(f'Средняя величина дохода сотрудников: {average_salary:.2f}')
