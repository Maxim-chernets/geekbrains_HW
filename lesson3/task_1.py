def func():
    a = float(input('Введите делимое:  '))
    b = float(input('Введите делитель:  '))
    div = a / b
    print(f'{div:.3f}')


try:
    func()
except ZeroDivisionError:
    print('На ноль делить нельзя')