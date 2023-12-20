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
       
        
    

print(somaPar)
print(somaTerceiraLista)
print(maiorValor)
