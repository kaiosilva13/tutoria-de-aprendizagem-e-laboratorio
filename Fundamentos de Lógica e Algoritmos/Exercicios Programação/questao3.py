valor_compra = float(input("Qual o valor total da compra? "))
if valor_compra < 500:
    valor_com_desconto = valor_compra * 0.95
    print(f"Sua compra inicialmente de R${valor_compra} com um desconto de 5% ficou pelo valor de R${valor_com_desconto}")
elif valor_compra <= 1000:
    valor_com_desconto = valor_compra * 0.90
    print(f"Sua compra inicialmente de R${valor_compra} com um desconto de 10% ficou pelo valor de R${valor_com_desconto}")
else:
    valor_com_desconto = valor_compra * 0.85
    print(f"Sua compra inicialmente de R${valor_compra} com um desconto de 15% ficou pelo valor de R${valor_com_desconto}")
