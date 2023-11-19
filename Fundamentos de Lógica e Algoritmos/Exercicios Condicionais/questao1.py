operacao = input("1 - Adição | 2 - Subtração | 3 - Multiplicação | 4 - Divisão |"
                 "5 - Potênciação | 6 - Divisão inteira\nQual a opção? ")
numero1 = float(input("Número 1: "))
numero2 = float(input("Número 2: "))
if operacao == "1":
    resultado = numero1 + numero2
    print(f"{numero1} + {numero2} = {resultado}")
elif operacao == "2":
    resultado = numero1 + numero2
    print(f"{numero1} - {numero2} = {resultado}")
elif operacao == "3":
    resultado = numero1 * numero2
    print(f"{numero1} * {numero2} = {resultado}")
elif operacao == "4":
    if numero2 == 0:
        print("Não é possível dividir por 0")
    else:
        resultado = numero1 / numero2
        print(f"{numero1} / {numero2} = {resultado}")
elif operacao == "5":
    resultado = numero1 ** numero2
    print(f"{numero1} ^ {numero2} = {resultado}")
elif operacao == "6":
    if numero2 == 0:
        print("Não é possível dividir por 0")
    else:
        resultado = numero1 // numero2
        print(f"{numero1} // {numero2} = {resultado}")
else:
    print("Opção inválida!")