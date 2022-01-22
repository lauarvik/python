#3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.

seasons_list = ['', 'зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
seasons_dict1 = dict(enumerate(seasons_list))
#seasons_dict1 = dict(enumerate(['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима'], 1))
seasons_dict2 = {
    'зима':[1,2,12], 
    'весна':[3,4,5], 
    'лето':[6,7,8], 
    'осень':[9,10,11],
}

month = 0
while not month in range(1,13):
    in_val = input("Введите номер месяца: ")
    if not in_val.isdigit(): continue
    month = int(in_val)

print(seasons_list[month])
print(seasons_dict1[month])

for k,v in seasons_dict2.items():
   if month in v:
       print(k)
       break
