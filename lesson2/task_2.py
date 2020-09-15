# input_list = input('Enter variables:  ')
# list_boom = list(input_list)
# print(list_boom)
my_list = []
number = int(input('Какое количество элементов в списке:  '))
for i in range(1, number+1):
    element = input(f'Введите элемент {i}:')
    my_list.append(element)
print(my_list)

for i in range(1, len(my_list), 2):
    el = my_list[i]
    my_list.insert(i-1, el)
    my_list.pop(i+1)
print(my_list)
