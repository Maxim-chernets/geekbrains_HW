
class MyEx(Exception):
    def __init__(self, txt):
        self.txt = txt

list = []

while True:
    number = input('Введите число:  ')
    if number == 'stop':
        break
    else:
        try:
            ask = number.isdigit()
            if number != 'stop' and ask != False:
                number = int(number)
                list.append(number)
            else:
                raise MyEx('Нужно вводить только числа!')
        except MyEx as err:
            print(err)
print(list)

# done