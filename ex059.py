"""

crie uma aplicacao que leia dois valores 
e mostre um menu na tela:

[1]somar
[2]multiplicar
[3]maior
[4]novos numeros
[5]sair do programa

"""
parada = 0

while parada <= 4:
    primeiroValor = int(input("Digite um numero: "))
    segundoValor = int(input("Digite outro numero: "))

    print("[1]somar")
    print("[2]multiplicar") 
    print("[3]maior") 
    print("[4]novos numeros") 
    print("[5]sair do programa")

    opcao = int(input("Selecione uma opcao de 1 a 5: "))
    escolha = opcao

    while primeiroValor > 0:
        if escolha == 1:
            print(primeiroValor + segundoValor)
            break
        elif escolha == 2:
            print(primeiroValor * segundoValor)
            break
        elif escolha == 3:
            if primeiroValor > segundoValor:
                print(primeiroValor)
            else:
                print(segundoValor)
                break
        elif escolha == 4:
            print("=-=" * 10)
            break
        elif opcao == 5:
            print ("Fim do programa")
            parada = 5
            break
        else:
            print("Opcao invalida! Tente novamente!")
    print("=-=" * 10)

###  
"""

resposta curso em video:

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opcao = 0
while opcao != 0:
    print("[1]somar
    [2]multiplicar 
    [3]maior 
    [4]novos numeros
    [5]sair do programa") ***usar tres aspas dentro do print aqui nao foi possivel devido a impossibilidade de usar tres asspas dentro do comentario***
    opcao = int(input("Qual a sua opcao: "))
    if opcao == 1:
    
    elif opcao == 2:
    
    elif opcao == 3:
    
    elif opcao == 4:
    
    elif opcao == 5:
    
    else:
        print("Opcao invalida! Tente novamente")
    else:
    print("=-=" * 10)
print("Fim do programa!")
"""