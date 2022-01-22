#5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

rating_list = [7, 5, 3, 3, 2]
rating_elem = int(input("Введите новый элемент рейтинга: "))

print(rating_list)

for k,v in enumerate(rating_list):
    if rating_elem > v:
        rating_list.insert(k, rating_elem)
        break
else:
    rating_list.append(rating_elem)

print(rating_list)
