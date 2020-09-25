with open('file_for_task_3.txt', 'r') as file:
    string = file.read()

list = string.split('\n')

list_new = []
for i in list:
    m = i.split(' ')
    list_new.append(m)

small_salary = []
for i in list_new:
    for z in i[1:]:
        z = int(z)


for i in list_new:
    for z in i[1:]:
        if z <= '20000':
            small_salary.append(i)

print ('Список сотрудников с зарплатой менее 20000:  ')
for i in small_salary:
    for z in i[:1]:
        print(z)

mean = 0
q = 0
for i in small_salary:
    for z in i[1:]:
        mean = mean + int(z)
        q += 1

print(f'Средняя зарплата сотрудников {mean/q:.3f}')

# done