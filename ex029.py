#Escreva um programa que leia a velocidade de um carro
#Se ele ultrapassar 80km/h mostre uma mensagem dizendo que foi multtado
#A multa vai custar 7 reais por cada quilometro acima excedido
#
velocidade = float(input("Qual a velocidade atual do carro? "))
limite = float(80)
if velocidade > limite:
    valor_multa = (velocidade - limite) * 7
    print("MULTADO! Velocidade excedida! O limite permitido e de 80km/h.")
    print("Valor da multa R${:.2f}!".format(valor_multa))
    print("Dirija com seguranca!")
else:
    print("Velocidade dentro do limite permitido. Boa viagem!")
