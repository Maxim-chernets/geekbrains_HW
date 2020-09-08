
time_sec = int(input('Введите время в секундах:   '))

hours = int(time_sec // 3600)
minutes = int(time_sec % 3600 // 60)
seconds = int(time_sec % 3600 % 60)

print(f'{hours} часов {minutes} минут {seconds} секунд')
