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


"""
resposta curso em video

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Name: ')))
    temp.append(float(input('Wheight: ')))
    if len(princ) == 0
        mai = men temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Continue? [S/N] '))
    if resp in 'Nn':
        break

print('=-*30)
print(f'In total you registered {len(princ)} people.')
print(f'The most havier was {mai}Kg.', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'the lowest weight was {men}Kg. ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()
    
"""