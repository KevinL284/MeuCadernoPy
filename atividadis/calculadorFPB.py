# Inicialização das variáveis
mat = [[1, 2, -1, 2, 3], [1, -3, 4, 2, 0], [0, -3, 5, 2, 3, 4]]
sl = [0, 0, 0]
x = 0

# Loop para somar os elementos da matriz
for i in range(3):
    for j in range(len(mat[i])):
        sl[i] += mat[i][j]
    x += sl[i]

print(x)
