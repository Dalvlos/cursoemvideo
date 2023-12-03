"""
faca uma aplicacao que leia um numero inteiro
e diga se ele e ou nao um numero primo.
"""
"""
numero = int(input("Digite um numero inteiro: "))

dois = 2

divisao = numero / dois

resto = numero % dois

if resto == 0:
    print("O numero {} nao e primo!".format(numero))
else:
    for primo in range(numero):
        numero / 3 or numero / 5 or numero / 7 or numero / 13 or numero / 17 != 0
    print("O numeo {} e um numero primo".format(numero)) 
"""

numero = int(input("Digite um numero inteiro: "))
tot = 0

for contador in range(1, numero +1):
    if numero % contador == 0:
        print("\033[33m", end=" ")
        tot += 1
    else:
        print("\033[31m", end=" ")
    print("{}".format(contador), end=" ")
print("\n\033[mO numero {} foi divisivel {} vezes".format(numero, tot))

if tot == 2:
    print(" E por isso e primo!")
else:
    print("E por isso nao e primo!")
