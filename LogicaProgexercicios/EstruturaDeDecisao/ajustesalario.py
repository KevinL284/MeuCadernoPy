# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

def valor_salario ():
    while True: 
        try:
            salario = float(input("Informe o valor do salário: "))
            break
        except ValueError:
            print("O valor informado não é um salário válido, por favor digite um salário válido.")
    return salario

salario = valor_salario()

if salario <= 280:
    salario *= 1.2
    percentual = 20
elif salario <= 700:
    salario *= 1.15
    percentual = 15
elif salario <= 1500:
    salario *= 1.1
    percentual = 10
else:
    salario *= 1.05
    percentual = 5
    
aumento = salario - salario / (1 + percentual / 100)

print(f"O salário antes do reajuste era de R${salario - aumento:.2f}")
print(f"O percentual de aumento aplicado foi de {percentual}%")
print(f"O valor do aumento foi de R${aumento:.2f}")
print(f"O novo salário, após o aumento, é de R${salario:.2f}")


