#2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.

def user_info(first_name, last_name, year_of_birth, city_of_living, email, phone_number):
    #вывод переменных f-строк в стиле {first_name=} - особенность Python3.8
    print(f"{first_name=}, {last_name=}, {year_of_birth=}, {city_of_living=}, {email=}, {phone_number=}")

user_info(first_name='Мария', last_name='Евдокимова', city_of_living='Сталинград', year_of_birth='2004', phone_number='+7 (8442) 60‒00‒20', email='mevdokimova@mail.ru')
