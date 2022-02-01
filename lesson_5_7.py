# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме:
# название, форма собственности, выручка, издержки.

import json

firms = {}
with open('lesson_5_7.txt', encoding='utf-8') as f:
    while 1:
        line = f.readline()
        if not line:
            break
        firm, form_of_ownership, revenue, outlay = line.split()
        #Прибыль компании
        profit = int(revenue) - int(outlay)
        firms[firm] = profit


profits = [x for x in firms.values() if x > 0]
average_profit = sum(profits) / len(profits)
result_list = [firms, {'average_profit': average_profit}]
print(result_list)

with open('lesson_5_7.json', 'w') as f:
    json.dump(result_list, f)
