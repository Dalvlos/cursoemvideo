"""
Faca uma aplicacao que leia 5 valores numericos
e guarde-os em uma lista.

No final mostre qual foi o maior e o menor valor
digitado e as suas respectivas posicoes na lista.
 


Resposta do curso em video:

listanum = []
mai = 0
men = 0

for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para a posicao {c}: ')))
    if c == 0:
        mai = men = lista[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('-='*30)
print(f'Voce digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posicoes', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men} nas posicoes ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
print()
"""

cincoNumeros = []
for i in range(0, 5):                
    cincoNumeros += [int(input("digite um numero: "))]

print('-='*40)   
print(f'Essa e a lista na ordem que o usuario digitou: {cincoNumeros}')
print('-='*40)
   
aposCinco = cincoNumeros.copy()

aposCinco.sort()
maior = aposCinco[-1]
menor = aposCinco[0]

valorMaior = maior 
valorMenor = menor

if valorMaior in cincoNumeros:
    posicao = cincoNumeros.index(valorMaior)
print(f'O maior numero que o usuario digitou foi {maior} na posicao {posicao}')

if valorMenor in cincoNumeros:
    posicao2 = cincoNumeros.index(valorMenor)
print(f'O menor numero digitado pelo usuario foi {menor} na posica {posicao2}')
