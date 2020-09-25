

dictionary = {
    'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'
}

with open('file_for_task_4_trans.txt', 'w', encoding='utf-8') as trans_file:
    with open('file_for_task_4.txt', 'r', encoding='utf-8') as file:
        strings = file.read().split('\n')
        for i in strings:
            i = i.split(' - ')
            trans_file.writelines(dictionary[i[0]] + ' - ' + i[1] + '\n')





