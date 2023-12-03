"""

Crie uma aplicacao que ira ler varios numeros e colocar em uma lista.

Depois disso crie duas listra extras que vao conter apenas os valores pares
e os valores impares digitados, respectivamente.

Ao final mostre o conteudo das tres listas geradas.

RESPOSTA CURSO EM VIDEO

num = list()
pares = list()
impares = list()

while True:
    num.apend(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v %2 == 0:
        pares.append(v)
    elif v %2 == 1:
        impares.append(v)

print('-='*30)
print(f'A lista completa e {num}')
print(f'A lista com numeros pares e {pares}')
print(f'A lista com numeros impares e {impares}')

"""

sequencie = []
while True:
    number = int(input('Enter a number: '))
    sequencie.append(number)
    variableOfStop = input('Do you wish to continue [Y/N]? ').lower()
    if variableOfStop == 'n':
        break

pairs = []
odd = []
for i in range(len(sequencie)):
    if i %2 == 0:
        pairs.append(i)
    else:
        odd.append(i)

print(sequencie)
print(pairs)
print(odd)