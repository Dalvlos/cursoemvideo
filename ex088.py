"""

Faca um programa que ajude um jogador da mega sena a criar palpites.
O programa vai perguntar quantos jogos serao gerados 
e vai sortear 6 numeros entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.


"""

import random

jogosRealizados = []

quantidadeJogos = int(input('Deseja gerar quantos Jogos? '))

i = 0

while i < quantidadeJogos:
    numeros = list(range(1, 61))
    lista_composta = []
    for _ in range(6):
        if numeros:
            escolha_aleatoria = random.choice(numeros)
            lista_composta.append(escolha_aleatoria)
            numeros.remove(escolha_aleatoria)        
    lista_composta.sort()
    jogosRealizados.append(lista_composta)
    i += 1

for jogo in jogosRealizados:
    print(jogo)

