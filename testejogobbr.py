
while True:
    # solicita ao usuário que insira um número inteiro
    numero = str(input("Digite um número inteiro de quatro dígitos: "))
    # verifica se a string contém apenas dígitos numéricos
    if numero.isdigit():
        # a string contém apenas dígitos numéricos, pode ser convertida em um número inteiro
        numero_int = int(numero)
    else:
        # a string contém caracteres não numéricos
        print("A entrada não é um número válido.")
    # verifica se o valor inserido contém quatro dígitos
    if len(numero) != 4:
        print("Erro: o número deve ter exatamente quatro dígitos.")
        continue

    # verifica se o valor inserido é um número inteiro
    try:
        numero = str(numero)
    except ValueError:
        print("Erro: o valor inserido não é um número inteiro.")
        continue

    # se chegou aqui, o valor inserido é válido
    break

# faz alguma coisa com o valor inserido
print(f"O número inserido foi: {numero}")

# converte o número inteiro em uma string
numero_str = str(numero)

# separa o número em três constantes usando slicing
constante1 = numero_str
constante2 = numero_str[1:]
constante3 = numero_str[2:]
constante4 = numero_str[:2]

# exibe as três constantes
print(f"Constante 1: {constante1}")
print(f"Constante 2: {constante2}")
print(f"Constante 3: {constante3}")
print(f"Constante 3: {constante4}")

# converte as constantes em inteiros
constante1_int = int(constante1)
constante2_int = int(constante2)
constante3_int = int(constante3)
constante4_int = int(constante4)

