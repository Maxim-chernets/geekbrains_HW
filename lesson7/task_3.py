class Cell:
    def __init__(self, numbers):
        self.numbers = numbers

    def __add__(self, other):
        return f'Сумма ячеек равно {self.numbers + other.numbers}'


    def __sub__(self, other):
        if self.numbers - other.numbers > 0:
            return self.numbers - other.numbers
        else:
            print('Ошибка')


    def __mul__(self, other):
        return f'Перемножение ячеек равно {self.numbers * other.numbers}'


    def __floordiv__(self, other):
        return f'Целое число от деления клеток {self.numbers // other.numbers}'


    def __str__(self):
        return self.numbers


    def make_order(self, rows):
        self.row = rows
        return '\n'.join(['*'* rows for _ in range(self.numbers//rows)]) + '\n' + '*' * (self.numbers % rows)


a = Cell(2)
b = Cell(5)
print(a+b)
print(a-b)
print(a*b)
print(a//b)

print(b.make_order(2))