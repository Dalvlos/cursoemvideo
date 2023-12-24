"""

aprimore o desafio anterior, mostrando no final:

a) A soma de todos os valores pares digitados

b)A soma dos valores da terceira coluna.

c) O maior valor da segunda coluna. 

"""

matriz = []

for liner in range(3):  
    linha = []  
    for columer in range(3):  
        valor = int(input(f"Digite o valor para a posição [{liner}][{columer}]: "))
        linha.append(valor)  
    matriz.append(linha) 
    

print("Matriz preenchida:")
for linha in matriz:
    print(linha)


somaPar = 0
for lista in matriz:
    for valor in lista:
        if valor % 2 == 0:
            somaPar += valor

terceiraLista = matriz[-1]
somaTerceiraLista = 0
for lista2 in terceiraLista:
    somaTerceiraLista += lista2
    

maiorValor = 0
segundaColuna = matriz[1]

for iteracao in segundaColuna:
    if iteracao > maiorValor:
        maiorValor = iteracao
       
        
    

print(f'A soma de todos os valores pares digitados: {somaPar}')
print(f'A soma dos valores da terceira coluna: {somaTerceiraLista}')
print(f'O maior valor da segunda coluna: {maiorValor}')


"""

Resolucao da aula do curso em video:

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-=' * 30):

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print(f'A soma do valores pares e {spar}')

for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna e {scol}.')

for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz [1] [c]
print(f'O maior valor da segunda linha e {mai}.')    


"""