"""
Refaca o exercicio 009,
mostrando a tabuada de um numero que o 
usuario escolher, so que agora utilizando
utilizando um laco for.
"""

number = int(input("insira um numero inteiro: "))

for tabuada in range(1, 11, 1):
    print("{} x {} = {}".format(number, tabuada, (number * tabuada)))
