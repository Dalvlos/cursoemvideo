#faca um programa que leia tres numeros
#e mostre qual e o maior e o menor

""" Resolucao CURSO em Video Python
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))
#verificando qual o valor menor
menor = a

if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#verificando qual o valor maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print("O menor valor digitado foi {}".format(menor))
print("O maior valor digitado foi {}".format(maior))

"""

primeiro_num = int(input("Insira um numero: "))
segundo_num = int(input("Insira outro numero: "))
terceiro_num = int(input("Insira mais um numero: "))

verificacao1 = primeiro_num >= segundo_num
verificacao2 = primeiro_num >= terceiro_num

verificacao3 = segundo_num >= terceiro_num
verificacao4 = segundo_num >= primeiro_num

verificacao5 = terceiro_num >= primeiro_num
verificacao6 = terceiro_num >= segundo_num

if verificacao1 and verificacao2 == True:
    print("O maior numero que voce digitou foi {}.".format(primeiro_num))
elif verificacao3 and verificacao4 == True:
    print("O maior numero que voce digitou foi {}.".format(segundo_num))
else: 
    verificacao5 and verificacao6 == True
    print("O maior numero que voce digitou foi {}.".format(terceiro_num))

verificacao7 = primeiro_num < segundo_num
verificacao8 = primeiro_num < terceiro_num

verificacao9 = segundo_num < terceiro_num
verificacao10 = segundo_num < primeiro_num

verificacao11 = terceiro_num < primeiro_num
verificacao12 = terceiro_num < segundo_num

if verificacao7 and verificacao8 == True:
    print("O menor numero que voce digitou foi {}.".format(primeiro_num))
elif verificacao9 and verificacao10 == True:
    print("O menor numero que voce digitou foi {}.".format(segundo_num))
else: 
    verificacao11 and verificacao12 == True
    print("O menor numero que voce digitou foi {}.".format(terceiro_num))

"""if verificacao1 and verificacao2 == False:
    print("O menor numero que voce digitou foi {}.".format(primeiro_num))
elif verificacao3 and verificacao4 == False:
    print("O menor numero que voce digitou foi {}.".format(segundo_num))
else: 
    verificacao5 and verificacao6 == False
    print("O menor numero que voce digitou foi {}.".format(terceiro_num))"""