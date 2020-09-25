
with open('file_for_task_6.txt', 'r', encoding='utf-8') as file:
        lessons = file.readlines()
        for i in lessons:
            number = ''.join((s if s in '1234567890' else ' ') for s in i)
            numbers = sum([int(i) for i in number.split()])
            print(f'{i.split()[0]} {numbers}')
