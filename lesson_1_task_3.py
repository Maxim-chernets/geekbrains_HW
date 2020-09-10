
number = None
while True:
    number = int(input('Введите число от 1 до 9:  '))
    if number >= 10 or number <= 0:
        print('Число должно быть от 1 до 9')
    else:
        break
number = number + number*11 + number*111
print(f'Ваше число в виде n + nn + nnn равно {number}')
