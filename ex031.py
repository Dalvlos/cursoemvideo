#desenvolva um programa que pergunte a distancia de uma viagem em Km
#calcule o preco da passagem cobrando 0,50 por quilometro  para viagens de ate 200km
#e 0.45 para viagens mais longas

"""viagemkm = float(input("Quantos km ira viajar? "))

valorkm050 = float(0.50 * viagemkm)

valorkm045 = float(0.45 * viagemkm)

if viagemkm <= 200:
    print("O valor total desta viagem custara R${:.2f}.".format(valorkm050))

else:
    print("O valor total desta viagem custara R${:.2f}.".format(valorkm045))
"""
distancia = float(input("Qual a distancia da viagem? "))
print("Voce ira viajar {}Km".format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print("sua passagem custara R${:.2f}".format(preco))
