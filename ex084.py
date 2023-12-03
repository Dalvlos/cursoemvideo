"""

faca uma aplicacao que leia o nome e peso de varias pessoas
guardando tudo em uma lista. No final, mostre:

a)Quantas pessoas foram cadastradas.

b)Uma listagem com as pessoas mais pesadas

c) uma listagem com as pessoas mais leves.

"""

lista = []
contagemCadastro = 0
while True:
    nome = str(input('digite o nome: '))
    peso = float(input('digite o peso: '))
    a = nome, peso
    lista.append(a)
    contagemCadastro += 1
    pausa = input('Desejesa inserir mais dados? s/n: ').upper()
    if pausa == 'N':
        break

lista_ordenada = sorted(lista, key=lambda x: x[1])
lista_ordenada2 = sorted(lista, key=lambda x: x[1], reverse=True)
    
print(f'Foram cadastradas {contagemCadastro} pessoas.')
print(f'As pessoas mais pesadas em ordem {lista_ordenada2}.')
print(f'As pessoas mais leves em ordem {lista_ordenada}.')


