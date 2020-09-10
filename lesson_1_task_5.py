
revenue = float(input('Какая выручка вашей конторы:  '))
costs = float(input('Сколько вы потратили:  '))

if costs > revenue:
    print('Вы работаете в убыток, вам нужно переосмыслить бизнес')
elif revenue > costs:
    team = int(input('Сколько сотрудников в вашей фирме:  '))
    profitability = revenue / costs * 100
    profit_per_employee = revenue / team
    print('Вы прибыльны!')
    print(f'Рентабильность равна {profitability:.2f}%')
    print(f'Каждый сотрдуник приносит вам в среднем ${profit_per_employee:.2f} ')
else:
    print('Ваша выручка равна издержкам. Еще чуток и капец!')
