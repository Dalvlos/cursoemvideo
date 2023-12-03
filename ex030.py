#Crie um programa que leia um numero inteiro
#e mostre na tela se este numero e par ou impar

numero = int(input("insira um numero: "))

if (numero%2) == 0:
    print("O numero {} e par!".format(numero))
else:
    print("O numero {} e impar!".format(numero))
