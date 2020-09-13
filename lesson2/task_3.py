dict_months = {
    1: 'Jan',
    2: 'feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'Aug',
    9: 'Sep',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec'
}

dict_seasons = {
    1: 'Winter',
    2: 'Winter',
    3: 'Spring',
    4: 'Spring',
    5: 'Spring',
    6: 'Summer',
    7: 'Summer',
    8: 'Summer',
    9: 'Fall',
    10: 'Fall',
    11: 'Fall',
    12: 'Winter'
}

while True:
    month = int(input('Введите номер месяца:'))
    if 0 < month < 13:
        break
    else:
        print('Вообще-то у нас всего 12 месяцев. Нужно от 1 до 12.')
print(dict_months.get(month))
print(dict_seasons.get(month))
