saysmth = None
strings = ''
while saysmth != '':
    saysmth = input('Напишите строку, которую нужно записать в файл:   ')
    strings = strings +'\n' + saysmth

strings = strings[1:]
with open('a_file.txt', 'w') as a_file:
    a_file.write(strings)

# done