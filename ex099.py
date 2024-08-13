"""
faça um programa que tenha uma função
chamada maior(), que receba varios parâmetros
com valores inteiros.

seu programa tem que analizar todos os valores e dizer
qual deles é o maior.

"""

def obter_maior_numero():
    lista_numeros_inteiros = []
    
    while True:
        try:
            numero = int(input('Digite um número inteiro: '))
            lista_numeros_inteiros.append(numero)
        except ValueError:
            print("Por favor, insira um número inteiro válido.")
            continue

        pausa = input('Deseja adicionar mais um número? (s/n): ').strip().lower()
        if pausa == 'n':
            break
    
    if lista_numeros_inteiros:
        maior_numero = max(lista_numeros_inteiros)
        print(f"O maior número na lista é: {maior_numero}")
    else:
        print("Nenhum número foi inserido.")

# Chamar a função
obter_maior_numero()
