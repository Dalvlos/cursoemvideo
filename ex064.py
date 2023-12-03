"""

crie um programa que leia varios numeros inteiros
pelo teclado. A aplicacao vai parar quando o usuario digitar 
o valor 999. que é a condicao de parada. no final, mostre quantos
numeros foram digitados e qual foi a soma entre eles. 
(desconsiderando o flag).

"""

n = c = soma = 0
n = int(input("Digite um numero inteiro [para parar digite 999]: "))
while n != 999:
    soma += n 
    c += 1
    n = int(input("Digite um numero inteiro [para parar digite 999]: "))
print("fim da execucao! Voce digitou {} numeros e a soma entre eles e {}".format(c, soma)) 

