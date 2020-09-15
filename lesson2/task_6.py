
data = []
corteg = []
i = 1
# item = input('Название товара:  ')
# price = float(input('Цена товара:  '))
# amount = int(input('Количество товара:  '))
# units = input('Единицы:  ')
ask = input('Хотите добавить новый товар в базу данных? да/нет:  ')
while ask == 'да':
    dictionary = {'Название': input('Название товара:  '), 'Цена': input('Цена товара:  '),
              'Кол-во': input('Количество товара:  '), 'Единицы': input('Единицы:  ')} # собираем словарь
    corteg.append(i)
    corteg.append(dictionary) # добавляем словарь в список
    corteg_transfer = tuple(corteg) # преобразуем список в кортеж
    data.append(corteg_transfer) # добавляем кортеж в список (БД)
    corteg.clear() # чистим список, для добавления новых словарей
    i += 1
    ask = input('Хотите добавить новый товар в базу данных? да/нет:  ')
else:
    print(data)

items = []
prices = []
amount = []
units = []
for i in range(0, len(data)):
    item = (data[i])[1].get('Название')
    items.append(item)
    items = set(items)
    items = list(items)
    price = (data[i])[1].get('Цена')
    prices.append(price)
    prices = set(prices)
    prices = list(prices)
    q = (data[i])[1].get('Кол-во')
    amount.append(q)
    amount = set(amount)
    amount = list(amount)
    unit = (data[i])[1].get('Единицы')
    units.append(unit)
    units = set(units)
    units = list(units)

analysis = {'Название': items,
            'Цены': prices,
            'Количество': amount,
            'Единицы': units}

print(analysis)

