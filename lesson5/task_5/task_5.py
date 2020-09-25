# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


with open('file_task_5.txt', 'w', encoding='utf-8') as file:
    numbers = file.write('2 45 67 -3 1')

with open('file_task_5.txt', 'r', encoding='utf-8') as file:
    digits = file.read()

list = digits.split(' ')

sum = 0
for i in list:
    i = int(i)
    sum += i

print(f'Сумма чисел равна {sum}')

# done