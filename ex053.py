"""
Crie uma aplicacao que leia uma frase qualquer
e diga se ela e um palindromo. considerando
os espacos.
"""

frase = str(input("insira uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = junto[::-1]
"""print("Voce digitou a frase {}".format(frase))"""
"""for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]"""
print("O inverso de {} e {}".format(junto, inverso))
if inverso == junto:
    print("Temos um palindromo!")
else:
    print("A frase nao forma um palindromo!")
