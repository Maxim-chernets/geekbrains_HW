def fuct(n):
    number = 1
    list = [i for i in range(1, n+1)]
    for i in list:
        number *= i
    yield number


for i in fuct(6):
    print(i)

