
list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list_copy = [i for i in list]

max = int(list[0]+1)
list_copy.insert(0, max)
print(list_copy)

list_2 = [i for i, m in zip(list, list_copy) if i > m]

print(list_2)

# done