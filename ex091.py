"""

Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios
Guarde esses resultados em um dicionario. No final, coloque esse dicionario em ordem
sabendo que o vencedor tirou o maior numero no dado.

"""
"""
import random

resultado = {}

player1 = random.randint(1, 6)
player2 = random.randint(1, 6)
player3 = random.randint(1, 6)
player4 = random.randint(1, 6)

resultado ['player1'] = player1
resultado ['player2'] = player2
resultado ['player3'] = player3
resultado ['player4'] = player4

resultadoOrdenado = dict(sorted(resultado.items(), key=lambda item: item[1], reverse = True))
print(resultadoOrdenado)
"""
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1' : randint(1, 6),
        'jogador2' : randint(1, 6),
        'jogador3' : randint(1, 6),
        'jogador4' : randint(1, 6),
        }
ranking = dict()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.33)
ranking = sorted(jogo.items(),key=itemgetter(1), reverse=True)
print(ranking)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(0.33)
