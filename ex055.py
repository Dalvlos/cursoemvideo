"""

Faca uma aplicacao que leia o peso 
de cinco pessoas. Ao final, mostre 
qual o maior e o menor peso lidos.

"""
maiorpeso = 0
menorpeso = 0

for p in range(1,6):
    peso = float(input("Informe o pesoa da pessoa {}: ".format(p)))
    if p == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print("O maior peso lido foi de {}Kg".format(maiorpeso)) 
print("O menor peso lido foi de {}Kg".format(menorpeso))
