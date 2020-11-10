class MyEx(Exception):
    def __init__(self, txt):
        self.txt = txt

number_1 = input('Введите делимое:  ')
number_2 = input('Введите делитель:  ')

try:
    number_1 = int(number_1)
    number_2 = int(number_2)
    if number_2 == 0:
        raise MyEx('На ноль делить нельзя!')
except (ValueError, MyEx) as err:
    print(err)
else:
    print(f'{number_1/number_2}')

# done