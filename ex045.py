"""crie um programa que faca 
o computador jogar jokenpo com voce
"""

from random import randint
from time import sleep


jokenpo = ("Pedra", "Papel", "Tesoura")

computador = randint(0,2)

print ("""Suas opcoes:
       [0] Pedra
       [1] Papel
       [2] Tesoura""")


jogador = int(input("escolha sua jogada: "))
print("Jo")
sleep(1)
print("Ken")
sleep(1)
print("Po")
sleep(2)
print("-=" * 20)

print(f"O computador jogou: {jokenpo[computador]}")
print(f"Jogador jogou: {jokenpo[jogador]}")
print("-=" * 20)

if computador == 0:
       if jogador == 0:
              print("EMPATE!")
       
       elif jogador == 1:
              print("VENCEU!")
       
       elif jogador == 2:
              print("PERDEU PARA O COMPUTADOR!")
       
       else:
              print("Jogada inexistente! Ecolha 0, 1 ou 2!")

elif computador == 1:
       if jogador == 0:
              print("PERDEU PARA O COMPUTADOR!")
       
       elif jogador == 1:
              print("EMPATE!")
       
       elif jogador == 2:
              print("VENCEU!")
       
       else:
              print("Jogada inexistente! Ecolha 0, 1 ou 2!")
              
elif computador == 2:
       if jogador == 0:
              print("VENCEU!")
       
       elif jogador == 1:
              print("PERDEU PARA O COMPUTADOR!")
       
       elif jogador == 2:
              print("EMPATE!")
       
       else:
              print("Jogada inexistente! Ecolha 0, 1 ou 2!")
    
