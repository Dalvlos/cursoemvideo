"""escreva um programa que leia dois numeros inteiros e o compare-os.
mostrando na tela uma mensagem:
-O primeiro valor e maior
-O segundo valor e maior
-Nao existe valor maior. Os dois sao iguais

resolucao curso em video python



"""
while True:
    primeiro_valor = int(input("Insira um numero inteiro: "))
    segundo_valor = int(input("Insira outro numero: "))

    if primeiro_valor > segundo_valor:
        print("O primeiro valor e maior")
    elif primeiro_valor == segundo_valor:
        print("Nao existe valor maior. Os dois sao iguais!")
    else:
        print("O segundo valor e maior.")
