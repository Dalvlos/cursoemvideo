"""

Crie um programa onde o usuario possa digitar 
cinco valores numericos ecadastre-os em uma lista
ja na posicao correta de incercao(sem usar o sort())

No final  mostre a lista ordenada na tela

RESPOSTA CURSO EM VIDEO:

lista = []

for c in range(0,5)
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[len[-1]]
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len():
            lista.insert(pos, n)
            print(f'Adicionado na posicao {pos} da lista...')
            brake
        pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')


"""
valoresCinco = []

for n in range(0,5):
    n = int(input('Digite um numero inteirno: '))
    valoresCinco.append(n)


print(sorted(valoresCinco))

