"""
Faca uma aplicacao que calcule 
a soma entre todos os numeros 
impares que sao multiplos de tres
e que se encontram no intervalo 
de 1 ate 500.
"""
total = 0
for n in range(1, 501, 2):
    if n %3 == 0: 
        total = n + total
print(total)