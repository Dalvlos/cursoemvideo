"""
Faca uma aplicacao onde o usuario possa digitar 
varios valores numericos e cadastre-sos em uma lista
Caso o numero ja exista na lista ele nao sera adicionado.

no final, serao exibidos todos os valores unicos
digitados em ordem crescente.

RESPOSTA CURSO EM VIDEO:

numeros = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor duplicado! Nao adionado')
    r = str(input('Quer continuar?'[S/N]))
    else:
    if r in 'Nn':
        break
print('=-'*30)
numeros.sort()
print(f'Voce digitou os valores {numeros}')

"""

print('Se quiser encerrar o programa digite -1')
print('=-'*30)
valoresUsuario = []
meusValores = []
while True:
    valoresUsuario.append(int(input('Digite um numero: ')))
    
    if -1 in valoresUsuario:
        meusValores = valoresUsuario
        break
meusValores = valoresUsuario[:-1]
conjuntoValores = set(meusValores)
print(conjuntoValores)