"""
Melhore o jogo do exercicio 028.
o computador ira escolher um numero
entre 0 e 10. so que agora o usuario 
vai tentar adivinhar ate acertar. 
mostrando ao final quantas tentativas 
foram necessaria para descobrir o numero escolhido
pelo computador.

"""

from random import randint
from time import sleep

computador = randint(0, 10)
print("Vou pensar em um numero entre 0 e 10. Tente adivinhar!")

jogador = int(input("Em que numero eu pensei? "))
print("PROCESSANDO...")
sleep(2)

contador = 0

while jogador != computador:
    print("Errou! tente um novo numero ate acertar: ")
    jogador = int(input("Em que numero eu pensei? "))
    if contador < 11:
        contador += 1        
    if jogador == computador:    
        print("Acerrtou! eu escolhi o numero {}, foram necessarias {} tentativas!".format(computador, contador))
