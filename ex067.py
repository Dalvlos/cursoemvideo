"""

Faca um programa que mostre a tabuada de varios numeros,
um de cada vez para cada valor digitado pelo usuario. 
O programa sera interrompido quando o numero solicitado
for negativo."""


n = int(input("Tabuada do numero: "))
i = 0
while i <= 9:
    i += 1
    r = n * i
    print("{} x {} = {}".format(n, i, r))

