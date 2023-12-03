"""
crie uma aplicacao que leia o ano
de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda nao atigiram
a maior idade e quantas ja sao maiores
"""

from datetime import date

atual = date.today().year
totalmaior = 0
totalmenor = 0

for pess in range(1, 8):
    nasc = int(input("digite o ano de nascimento da pessoa {}: ".format(pess)))
    idade = atual - nasc
    if idade >= 18:
        totalmaior += 1
    else:
        totalmenor += 1
    
print("Ao todo ha {} pessoas maiores de idade".format(totalmaior))
print("E ha tambem {} pessoas menores de idade".format(totalmenor))
"""pessoa2 = int(input("digite o ano de nascimento da pessoa 2: "))

pessoa3 = int(input("digite o ano de nascimento da pessoa 3: "))

pessoa4 = int(input("digite o ano de nascimento da pessoa 4: "))

pessoa5 = int(input("digite o ano de nascimento da pessoa 5: "))

pessoa6 = int(input("digite o ano de nascimento da pessoa 6: "))

pessoa7 = int(input("digite o ano de nascimento da pessoa 7: "))"""
