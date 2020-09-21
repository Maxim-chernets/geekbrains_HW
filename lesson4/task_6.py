from itertools import count, cycle

def func_count():
    number_start = int(input('C какого числа начинать список?  '))
    number_final = int(input('До какого числа продолжить список?  '))
    for el in count(number_start):
        if el > number_final:
            break
        else:
            print(el)

def func_cycle():
    foo = input('Введите элементы списка:')
    bar = int(input('Введите число, сколько раз будем перебрать элементы списка:  '))
    с = 0
    for el in cycle(foo):
        if с > bar:
            break
        print(el)
        с += 1


print('Итератор 1: Генерирует целые числа, начиная с указанного\nИтератор 2: Повторяет элементы списка.' )
choice = input('Введите 1, для запуска первого итератора или\nВведите 2, для запуска второго итератора:  ')

if choice == '1':
    func_count()

elif choice == '2':
    func_cycle()

else:
    print('Ошибка! Нужно ввести 1 или 2.')


# done
