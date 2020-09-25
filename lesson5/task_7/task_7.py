import json

with open('file_for_task_7.txt', 'w', encoding='utf-8') as file:
    companies = ['Brooms ПАО 2500000 500000\n', 'Tandoor АО 1245000 1880000\n', 'Honey-cake ЗАО 5250000 455000\n',
                 'Matrioshka OOO 4770000 511000\n', 'Сказка ИП 10500000 5000000\n']
    file.writelines(companies)

top_list = []
with open('json_file.json', 'w', encoding='utf-8') as json_file:
    with open('file_for_task_7.txt', 'r', encoding='utf-8') as file:
        profit = {}
        for line in file:
            profit[line.split(' ')[0]] = int(line.split(' ')[2]) - int(line.split(' ')[3])

        av_profit = sum([int(i) for i in profit.values() if int(i) > 0]) / len([int(i) for i in profit.values() if int(i) > 0])
        top_list.append(profit)
        top_list.append({'av_profit': round(av_profit)})
    json.dump(top_list, json_file, ensure_ascii=False)
