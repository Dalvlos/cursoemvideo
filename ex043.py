"""Desenvolva uma logica que leia o peso e a altura de uma pessoa
calcule o seu IMC e mostre seu status, de acordo com a tabela abaixo:

-abaixo de 18.5:Abaixo do peso
-entre 18.5 e 25:Peso ideal
-25 ate 35:Sobrepeso
-30 ate 40:Obesidade
-acima de 40:Obesidade morbida
"""

    
peso = float(input("Digite o peso (kg): "))
altura = float(input("Dgite a altura: "))

imc = peso / (altura * altura)

print("O seu peso e de {:.1f}, sua altura e de {:.2f}. Seu imc e de {:.1f}".format(peso, altura, imc))

if imc < 18.5:
    print("Abaixo do peso.")
elif imc < 25:
    print("Peso ideal.")
elif imc < 35:
    print("Sobrepeso.")
elif imc < 40:
    print("Obesidade.")
else:
    print("Obesidade morbida.")
