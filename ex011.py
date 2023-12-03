largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
area = largura * altura
print("A parede possui a dimensao de {} x {} e sua area e de {}m3.".format(largura, altura, area))
tinta = area / 2
print ("Para pintar essa parede sera necessario {} litros de tinta".format(tinta))