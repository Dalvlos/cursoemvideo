"""
Crie uma aplicacao que vai gerar cinco
numeros aleatorios e colocar em uma tupla.

depois disso, mostre a listagem de numeros gerados
e tambem indique o menor e o maior valor que estao
na tupla.
"""

from random import randint

aleatorio5 = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Os valores sorteados foram: ', end='')

for n in aleatorio5:
    print(f'{n} ', end='')

print(f'\nO maior valor sorteado foi: {max(aleatorio5)}')
print(f'O menor valor sorteado foi: {min(aleatorio5)}')
# print(f'Os valores sorteado foram {aleatorio5}')
# print()
