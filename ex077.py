"""
Crie um programa que tenha uma tupla com varias palavras
(nao use acentos)
Depois disso voce deve mostarar para cada palavra quais 
sao suas vogais.
"""

palavras = ('algebra', 'abacaxi', 'palito', 'gato', 'casa', 'roupa', 'motor', 'escola', 'zirconio')

vogais = ('a', 'e', 'i', 'o', 'u')

for p in palavras:
    print(f'\nNa a palavra {p} temos a seguintes vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')
            