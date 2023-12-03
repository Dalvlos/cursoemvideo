"""from math import hypot
cat_o = float(input("digite o valor do cateto oposto: "))
cat_a = float(input("digite o valor do cateto adjacente: "))
hi = (cat_o ** 2 + cat_a ** 2) ** (1/2)
print("a hipotenusa vai medir {:.2f}".format(hi))"""
import math ##you can use from math import hypot. and not necessary use reference math at variable hi. 
cat_o = float(input("digite o valor do cateto oposto: "))
cat_a = float(input("digite o valor do cateto adjacente: "))
hi = math.hypot(cat_o, cat_a)
print(hi)
