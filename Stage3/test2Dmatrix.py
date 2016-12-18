matrix = [[0 for i in range(3)] for i in range(3)]
print(matrix)
matrix[2][2] = 5
print(matrix)
matrix2 = [['shit' for j in range(3)] for j in range(4)]
print(matrix2)
matrix2[3][2] = 'good'
print(matrix2)
x = open('tese2D_matrix.txt','w')
for each in matrix2:
    print(each, file = x)
x.close()