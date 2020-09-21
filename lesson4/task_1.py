from sys import argv

name, hours, rate, bonus = argv
print(argv)


def salary():
    money = int(hours)*int(rate) + int(bonus)
    print(money)


salary()
# done