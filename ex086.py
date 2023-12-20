"""

crie um programa que crie uma matriz de dimensao 3x3
e preencha com valores lidos pelos teclado.

[0][0][0]
[0][0][0]
[0][0][0]

No final mostre na tela, com a formatacao correta.


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
