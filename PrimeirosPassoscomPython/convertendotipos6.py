# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool

print(1 + 1) # Soma padrão de int
print('a' + 'b') # Concatenação normal

print('1' + 1) # Erro de tipo por ser str e int e não dois int's


print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(' '))
print(str(11) + 'b')

