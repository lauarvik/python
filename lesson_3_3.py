#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

#решение с переменным числом аргументов, возврат суммы двух наибольших
# (Я испытываю слабость к универсальным решениям, где надо и не надо)
#def my_func2(*args):
#    my_list = list(args)
#    my_list.sort(reverse=True)
#    return sum(my_list[:2])

def my_func(n1, n2, n3):
    my_list = [n1, n2, n3]
    my_list.sort(reverse=True)
    return sum(my_list[:2])


print(my_func(1000, 1, 200))
