def converter_temperatura():
    escala = input("Escolha entre C, K ou F: ")
    temperatura = float(input("Qual a temperatura? "))

    if escala.upper() == "C":
        temp_f = (temperatura * 9/5) + 32
        temp_k = temperatura + 273.15
        print(f"A temperatura em F é {format(temp_f, '.2f')} e em K é {format(temp_k, '.2f')}")

    elif escala.upper() == "F":
        temp_c = (temperatura - 32) * 5/9
        temp_k = temp_c + 273.15
        print(f"A temperatura em C é {format(temp_c, '.2f')} e em K é {format(temp_k, '.2f')}")

    elif escala.upper() == "K":
        temp_c = temperatura - 273.15
        temp_f = (temp_c * 9/5) + 32
        print(f"A temperatura em C é {format(temp_c, '.2f')} e em F é {format(temp_f, '.2f')}")

    else:
        print("Escala inválida. Por favor, escolha entre C, K ou F.")

converter_temperatura()