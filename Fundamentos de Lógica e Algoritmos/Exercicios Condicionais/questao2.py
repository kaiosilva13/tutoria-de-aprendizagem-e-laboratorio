medida_lado1 = float(input("Digite a primeira medida do triângulo: "))
medida_lado2 = float(input("Digite a segunda medida do triângulo: "))
medida_lado3 = float(input("Digite a terceira medida do triângulo: "))
if medida_lado1 == medida_lado2 == medida_lado3:
    print("Classificação: Triângulo equilátero")
elif medida_lado1 == medida_lado2 or medida_lado1 == medida_lado3 or medida_lado2 == medida_lado3:
    print("Classificação: Triângulo isósceles")
else:
    print("Classificação: Triângulo escaleno")
