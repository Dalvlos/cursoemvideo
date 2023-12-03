#escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
#para salarios superiores a 1.250.00 calcule um aumento de 10%
#para os inferiores ou iguais o aumento e de 15%
"""Resolucao curso em video python

salario = float(input("Qual o salario do funcionario? R$"))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
alse:
    novo = salario + (salario * 10 / 100)    
print("O salario que era de R${:.2f} passou a ser de {:.2f}!".format(salario, novo))

"""

salario = float(input("Qual o salario do funcionario? R$"))

aumento10 = (salario * 10 ) / 100 + (salario) 
aumento15 = (salario * 15) / 100  + (salario)

if salario <= 1250.00:
    print("O funcionario ganhou um aumento de 15 porcento e passara a receber R${:.2f} ".format(aumento15))
else:
    print("O funcionario ganhou um aumento de 10 porcento e passara a receber R${:.2f} ".format(aumento10))
