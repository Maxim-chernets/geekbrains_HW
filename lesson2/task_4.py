my_str = input('Введите строку:  ')
my_str = my_str.split(' ') # приводим к списку, разделитель пробел

count = 1
for i in my_str:
    print(f'{count} {i:.10}')
    count += 1
