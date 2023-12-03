"""Escreva uma aplicacao que leia um numero inteiro qualquer 
e peca para o usuario escolher qual sera a base de conversao:
-1 para binario
-2 para octal
-3 para exadecimal
"""
while True: 
    n = int(input('Digite um número: '))
    print('- - - - '* 5)
    print('[1] Binário')
    print('[2] Octal')
    print('[3] Hexadecimal')
    print('[x] Sair')


    perguntanum = str(input('Digite a opção que deseja converter: '))
    
    
    if perguntanum == 'x'or perguntanum == 'X':
        break
    
    elif perguntanum == '1' or perguntanum == '2' or perguntanum == '3':        
        if perguntanum == '1':
            rio = str(bin(n))
            print(rio)   
        elif perguntanum == '2':
            cta = str(oct(n))
            print(cta)
        elif perguntanum == '3':
            exa = str(hex(n))
            print(exa)

    else:
        print('Opção invalida!')


""" Resolucao do curso em video

num = int(input("Digite um numero inteiro: "))

print('''Escolha uma das bases de conversao: 
[1] converter para BINARIO
[2] converter para OCTAL
[3] conveter para HEXADECIMAL''')
opcao = int(input("Sua opcao: "))

if opcao == 1:
    print("{} convertido para BINARIO e igual a {}".format(num, bin(num)[2:]))
elif opcao == 2:
    print("{} convertido para OCTAL e igual a {}".format(num, oct(num)[2:]))
elif opcao == 3:
    print("{} convertido para HEXADECIMAL e igual a {}".format(num, hex(num)[2:]))
else:
    print("Opcao invalida. tente novamente!")
"""