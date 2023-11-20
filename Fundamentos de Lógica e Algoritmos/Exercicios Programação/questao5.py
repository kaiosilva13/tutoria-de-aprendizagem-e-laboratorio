nota_1 = float(input("Nota 1° Bimestre: "))
nota_2 = float(input("Nota 2° Bimestre: "))
nota_3 = float(input("Nota 3° Bimestre: "))
nota_4 = float(input("Nota 4° Bimestre: "))
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
if media > 6:
    print(f"Parabéns! Você ficou com nota acima da média. Sua média foi de {media}")
elif media < 6:
    print(f"Infelizmente você ficou com nota abaixo da média. Sua média foi de {media}")
else:
    print(f"Você ficou com nota exatamente na média. Sua média foi de {media}")