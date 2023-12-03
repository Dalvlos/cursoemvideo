"""

Crie um programa que leia a idade e o sexo de varios pessoas.
A cada pessoa cadastrada o programa devera perguntar se o usuario
quer ou nao continuar. No final mostre:

a - quantas pessoas tem mais de 18 anos.
b- Quantos homens foram cadastrados.
c- Quantas mulheres tem menos de 20 anos.

"""
controle = str("s").upper()
while controle == "s":
    nome = str(input("Informe seu nome: "))
    idade = int(input("Informe sua idade: "))
    sexo = str(input("informe o sexo M/F: ")).upper()
    continuar_execucao = str(input("deseja continuar S/N: ")).upper()
    if continuar_execucao == "S":
        controle = "S"
    else:
        controle = "N"
    print(nome, idade, sexo)




