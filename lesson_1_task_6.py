
a = int(input('Сколько километров вы пробежали в первый день: '))
b = int(input('Сколько километров вы хотите пробежать: '))
day = 1
while a < b:
    if a < b:
        a = a*1.1
        day += 1
    else:
        break
print(f'Вы пробежите не менее {b} киллометров на {day}й день')