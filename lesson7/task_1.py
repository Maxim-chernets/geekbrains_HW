
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix



    def __str__(self):
        return f'{self.matrix[0][0]} {self.matrix[1][0]} {self.matrix[2][0]} \n{self.matrix[0][1]} {self.matrix[1][1]} {self.matrix[2][1]}'



    def __add__(self, other):
        list_1 = []
        for i in range(len(self.matrix)):
            list_1.append([])
            for m in range(len(self.matrix[0])):
                list_1[i].append(self.matrix[i][m] + other.matrix[i][m])
        return f'{list_1[0][0]} {list_1[1][0]} {list_1[2][0]} \n{list_1[0][1]} {list_1[1][1]} {list_1[2][1]}'

m_1 = Matrix([[1, 2], [3, 4], [5, 6]])
m_2 = Matrix([[4, 5], [3, 7], [3, 5]])
print(m_1)
print(m_2)
print(m_1+m_2)
# print(type(m_1+m_2))

# done