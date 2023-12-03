"""

crie um programa que leia varios numeros inteiros pelo teclado
O programa so vai parar quando o usuario digitar o valor 999
que e a condicao de parada. No final, mostre quantos numeros
foram digitados e qual foi a soma entre eles.(desconsiderando o Flag)

"""

numero = int(input("insira um numero inteiro: "))
cont = 0
total = 0
while numero != 999:
    numero
    cont += 1
    total += numero 
    print("se deseja sair do programa digite 999")
print("foram inseridos {} numeros e a sua soma de {}".format(cont, total))    