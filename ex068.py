"""

Faca um programa que jogue par ou impar com o computador.
o jogo sera interrompido quando o jogador perder, mostrando 
o total de vitoria consecutivas que ele consquistou no final do jogo.

"""

import random

vitoria = 0
derrotas = 0
while derrotas < 1:
    vitoria = 0
    derrotas = 0
    par_ou_impar = str(input("Vamos jogar par ou impar! Digite P para par ou I para impar: "))
    par_ou_impar_numero = int(input("Agora escolha um numero: "))
    numero_aleatorio = random.randint(0, 9)
    soma = par_ou_impar_numero + numero_aleatorio
    if soma % 2 == 0 and par_ou_impar == "Pp":
        vitoria += 1
    else:     
        derrotas += 1
    
    if soma % 2 == 1 and par_ou_impar == "Ii":
        vitoria += 1
    else:     
        derrotas += 1
    
    print ("Voce escolheu o numero {} e o computador o numero {}".format(par_ou_impar_numero, numero_aleatorio))


print("O jogo acabou! Voce venceu o computador {} vezes consecutivas".format(vitoria))