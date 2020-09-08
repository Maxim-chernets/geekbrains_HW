
number_max = 0
number = int(input('Введите целое положительное число:   '))
while number != 0:
    number_q = number % 10
    if number_q >= number_max:
        number_max = number_q
        number = number // 10
    elif number_q < number_max:
        number = number // 10

print(number_max)