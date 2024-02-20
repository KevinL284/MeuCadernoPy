import math

def calcular_sequencia(n):
    seq1 = sum([math.factorial(n-i) / (math.factorial(n-i-1) if n-i-1 >= 0 else 1) for i in range(n+1)])
    seq2 = sum([(2*i)**2 for i in range(n+1)])
    return seq1 + seq2

print(calcular_sequencia(4))