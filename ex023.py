
##numero = int(input("informe um numero: "))
#n = str(numero)
#print("Analisando o numero {}".format(numero))
#print("Unidade {}".format(n[3]))
#print("Dezena {}".format(n[2]))
#print("Centena {}".format(n[1]))
#print("Milhar {}".format(n[0]))#

numero = int(input("informe um numero: "))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print("Analisando o numero {}".format(numero))
print("Unidade {}".format(u))
print("Dezena {}".format(d))
print("Centena {}".format(c))
print("Milhar {}".format(m))
