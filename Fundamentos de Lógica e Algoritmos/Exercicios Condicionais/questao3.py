velocidade = float(input("Qual a velocidade em km/h: "))
if velocidade > 100:
    velocidade_ultrapassada = velocidade - 100
    multa = 1.50 * velocidade_ultrapassada
    print(f"Você ultrapassou {velocidade_ultrapassada} km/h e pagará uma multa de {multa} R$")
else:
    print("Você está dentro do limite de velocidade! Boa viagem.")