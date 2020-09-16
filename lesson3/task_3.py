# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func():
    numbers = [a, b, c]
    print(numbers)
    minimal = min(numbers)
    numbers.remove(minimal)
    numbers = sum(numbers)
    print(numbers)


try:
    a = float(input('Введите число a:  '))
except ValueError:
    print('Нужно вводить ЧИСЛО!')
try:
    b = float(input('Введите число b:  '))
except ValueError:
    print('Нужно вводить ЧИСЛО!')

try:
    c = float(input('Введите число c:  '))
except ValueError:
    print('Нужно вводить ЧИСЛО!')

try:
    my_func()
except NameError:
    print('Ошибка! Все аргументы должны быть числом')



