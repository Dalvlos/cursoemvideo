"""

Melhore o exercicio 061, perguntando 
ao usuario se ele quer mostrar mais
alguns termos. O programa encerra quando ele disser
que quer mostrar 0 termos.

"""



primeiro = int(input("primeiro termo: "))
razao = int(input("Razao: "))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print("{}".format(c))
termos = int(input("Deseja mostrar mais termos? "))
 
