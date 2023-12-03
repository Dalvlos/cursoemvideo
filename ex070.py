"""

crie um programa que leia o nome e o preco de varios produtos.
O programa devera perguntar se o usuario vai continuar.
no final mostre:

a- qual o total gasto na compra.
b- quantos produtos custam mais de R$1000
c- qual o nome do produto mais barato

"""
total = totmil = menor = cont = 0
barato = " "
while True:
    produto = str(input("Nome do Produto: "))
    preco = float(input("Preco: R$"))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print("{:-^40}".format("Programa encerrado!"))
print(f"O total da compra foi de R${total:.2f}")
print(f"Temos {totmil} produtos custando  mais de R$1000.00")
print(f"O produto mais barato foi {barato} que custa R${menor:.2f}")

    