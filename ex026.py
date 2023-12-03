frase = str(input("Digite uma frase: ")).strip()
fraseM = frase.upper()
print("A letra A aparece {} vezes na frase.".format(fraseM.count("A")))
print("A letra A aparece pela primeira vez na posicao {}".format(fraseM.find("A")))
print("A letra A aparece pela ultima vez na {} posicao".format(fraseM.rfind("A")))
     