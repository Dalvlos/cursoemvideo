"""

Faca uma aplicacao que leia um numero
qualquer e mostre o seu fatorial.

ex:
5! = 5x4x3x2x1 = 120

"""

"""
from math import factorial
numero = int(input("Insira um numero para calular o fatorial: "))
fac = factorial(numero)
print("O fatorial de {} é {}.".format(numero, fac))

"""

n = int(input("Insira um numero para calular o fatorial: "))
c = n
f = 1
while c > 0:
    print("{}".format(c), end="")
    print(" x " if c > 1 else " = ", end ="")
    f = f * c
    c -= 1
print("{}".format(f))
#print("O fatorial de {} é {}.".format(numero, fac))