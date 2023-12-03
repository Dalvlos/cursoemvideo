from math import radians, sin, cos, tan
import math

an = float(input("digite o angulo: "))
seno = math.sin(math.radians(an))

print("O angulo de {} tem o seno de {:.2f}".format(an, seno))
cosseno = math.cos(math.radians(an))

print("O angulo de {} tem o cosseno de {:.2f}".format(an, cosseno))
tangente = math.tan(math.radians(an))

print("O angulo de {} tem a tangente de {:.2f}".format(an, tangente))