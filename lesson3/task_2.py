def person(name, second_name, date, city, tel, email):
    print(f"Вас зовут {second_name} {name}, родился в {city} в {date} году. Контакты: {email}, {tel}")


try:
    person(name=input('Введите имя:  '),
           second_name=input('Введите фамилию:  '),
           date=int(input('Введите год рождения:  ')),
           city=input('Введите город:  '),
           tel=input('Введите телефон:  '),
           email=input('Введите имейл:  '))
except ValueError:
    print('Год рождения должен быть написан цифрами')
