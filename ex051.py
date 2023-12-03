"""
Desenvolva uma aplicacao que leia 
o primeiro termo e a razao de uma progressao aritimetica.
Ao final, mostre os 10 primeiros termos dessa progressao.

"""

a1 = int(input("Isira o primeiro termo da progressao: "))

r = int(input("insira a razao: "))

for razao in range(1, 11):
    an = a1 + (razao -1) * r
    print (an)

"""
resolucao curso em video

primeiro = int(input("primeiro termo: "))
razao = int(input("Razao: "))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print("{}".format(c), end="=- ")
print("Acabou")
"""
