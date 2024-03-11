#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

def obter_turno():
    while True:
        turno = input("Informe o turno em que você estuda (M-matutino ou V-Vespertino ou N- Noturno): ").upper()
        if turno == "M" or turno == "V" or turno == "N":
            break
        else:
            print("Valor inválido, por favor informe um valor válido.")
    return turno

turno = obter_turno()

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
else:
    print("Boa noite!")