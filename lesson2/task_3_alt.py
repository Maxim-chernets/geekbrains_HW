seasons = ['Winter', 'Spring', 'Summer', 'Fall']

while True:
    month_number = int(input('Введите номер месяца:'))
    if 0 < month_number < 13:
        break
    else:
        print('Вообще-то у нас всего 12 месяцев. Нужно от 1 до 12.')

if 9 <= month_number <= 11:
    print(seasons[3])
elif 3 <= month_number <= 5:
    print(seasons[1])
elif 6 <= month_number <= 8:
    print(seasons[2])
else:
    print(seasons[0])
