"""
desenvolva um programa que leia quatro valores pelo teclado 
e guarde-os  em uma mesma tupla. No final mostre:
a)quantas vezes apareceu o valor 9.
b)Em que posicao foi digitado o primeiro valor 3.
c)Quais foram os numeros pares.
--------------------------------------------------------------------------------
"""

quatroNumeros = (int(input("digite um numero: ")),
                 int(input("digite um numero: ")),
                 int(input("digite um numero: ")),
                 int(input("digite um numero: ")))
print(f'Voce digitou os valores {quatroNumeros}')
print(f'O valor 9 apareceu {quatroNumeros.count(9)} vezes')
if 3 in quatroNumeros:
    print(f'O numero 3 foi digitado na posicao {quatroNumeros.index(3)+1} da tupla')
else:
    print('O valor 3 nao foi digitado em nenhuma posicao')
numerosPares = []
n = 0
for n in quatroNumeros:
    if n % 2 == 0:
        numerosPares.append(n)
print(f'Os numero pares inseridos na tupla: {numerosPares}.', end=" ")
