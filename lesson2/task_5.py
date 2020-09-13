my_list = [6, 4, 2, 2, 1]
number = int(input('введите число:  '))
for i in range(0, len(my_list)):
    el = my_list[i]
    if number > el:
        my_list.insert(i, number)
        break
    elif number <= el:
        continue
print(my_list)
