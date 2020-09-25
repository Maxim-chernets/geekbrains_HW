with open('file_for_task_2.txt', 'r') as file:
    string = file.read()

list = string.split('\n')
q_strings = len(list)
print(f'В файле {q_strings} строки')

q_words = 1
number_str = 0
for i in list:
    if i == '':
        q_words = 0
    for x in i:
        if x == ' ':
            q_words += 1
    number_str += 1
    print(f'В {number_str}й строке {q_words} слова')
    q_words = 1

# done