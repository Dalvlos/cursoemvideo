"""

Desenvolva uma aplicacao que leia varios 
numeros inteiros pelo teclado. No final 
da execucao mostre a media entre todos os valores
 e qual foi o maior e o menor valores lidos.
 O programa deve perguntar ao usuario se ele quer ou nao
 cuntinuar a digitar valores. 

"""


pergunta = "S"
soma = quant = media = maior = menor = 0
while pergunta in "Ss":
    numero = int(input("Digite um numero inteiro:"))
    soma += numero
    quant += 1
    if quant == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero 
    pergunta = str(input("Deseja continuar? (s/n): ")).upper().strip()[0]
media = soma / quant
print("Foram digitados {} numeros. A media dos numeros digitados foi {}".format(quant, media))
print("O maior valor digitado foi {} e o menor foi {}".format(maior, menor))

