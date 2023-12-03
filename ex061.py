"""

refaca o exercico 051, lendo o 
primeiro termo e a razao de uma pa
mostrando os 10 primeiros termos
da progressao usando a estrutura
while.

"""

primeiro = int(input("primeiro termo: "))
razao = int(input("Razao: "))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print("{}".format(c), end="=- ")


