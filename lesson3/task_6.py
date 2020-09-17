def my_func():
    global title_word
    title_word = word.title()


string = input('Введите строку:   ')
string = string.split(' ')

string_try = ''.join(string) # с 9 по 18 строку - проверка на латиницу
list(string_try)

check = 0
for i in range(1, len(string_try)):
    if 97 <= ord(string_try[i]) <= 122:
        check += 1
        continue
    else:
        break
if check == i:
    title_string = ''
    for i in range(0, len(string)):
        word = string[i]
        my_func()
        title_string += (title_word + ' ')

    print(title_string)

else:
    print('Должны быть латинские буквы')

