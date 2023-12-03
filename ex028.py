#Escreva uma aplicacao que faca o escolher um numero inteiro de 0 a 5
#e peca para o usuario tentar descobrir qual foi o numero escolhido pelo computador
#O programa devera escrever na tela se o usuario venceu ou perdeu
from random import randint
from time import sleep
computador = randint(0, 5)
print("Vou pensar em um numero entre 0 e 5. Tente adivinhar!")
Jogador = int(input("Em que numero eu pensei? "))
print("PROCESSANDO...")
sleep(2)
if Jogador == computador:
    print("Parabens! Acertou!!!")
else:
    print("Errou! Excolhi o numero {} e voce {}. Tente novamente!".format(computador, Jogador))
