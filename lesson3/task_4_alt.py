def my_func(x, i):
    final_number = 1
    y = i
    while i != 0:
        number = 1 / x
        final_number = final_number * number
        i += 1
    else:
        print(f'({x} в степень {y} равно {final_number:.4}')



x = float(input('Введите дейтсвительное положительное число: '))
i = int(input('Введите целое отрицательное число: '))


my_func(x, i)
