"""

Crie uma aplicacao que vai ler varios numeros 
e colocar em uma lista.
depois disso, mostre:

a)Quantos numeros foram digitados.
b)A lista de valores ordenada de forma decrescente
c)Se o valor 5 foi digitado e esta ou nao na lista.

RESPOSTA CURSO EM VIDEO:

valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print('=-'*30)
print(f'Voce digitou {len(valores)} elementos.')
valores.sort(reverse = True)
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 nao foi encontrado na lista!')

"""
print('Digite -1 para encerrar a aplicacao... ')
print('=-'*30)

lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n == -1:
        break
lista.remove(-1)

ordenada = sorted(lista.copy())

ordenada.reverse()

print(f'Foram digitados {len(ordenada)} numeros... ')

print(f'Esta e a lista decrescente: {ordenada}...')

elemento = 5
if elemento in ordenada:
    print(f"{elemento} está na lista.")
else:
    print(f"O numero {elemento} não foi incluido na lista.")