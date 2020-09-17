
total = 0
stop = 0
while stop != 1:
    numbers = input('Введите числа через пробел.\nДля завершения введите q:    ')
    numbers = numbers.split(' ')
    list = []
    for i in range(0, len(numbers)):
        if numbers[i].isdigit():
            digit = int(numbers[i])
            list.append(digit)
        elif numbers[i] == 'q':
            stop = 1
            print('Вы завершили программу')
            break
        else:
            continue
    summa = sum(list)
    total = total + summa
    print(list)
    print(f'Сумма чисел равна {summa}, общая сумма равна {total}')

