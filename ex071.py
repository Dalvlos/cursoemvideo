"""

crie um programa que simule o funcionamento de um caixa eletronico.
No inicio pergunte ao usuario qual sera o valor a ser sacado (numero inteiro)
e o programa vai informar quantas cedulas200 de cada valor serao entregues.

obs: considere que o caixa possui cedulas200 de R$50, R$20, R$10 e R$1.

print("="*30)
print("Python Bank")
print("="*30)
saque = int(input("Qual volor de saque? "))

if saque > 200:
    cedulas200 = saque // 200
    primeiroValorRestante = saque % 200
    print(f"Total de {cedulas200} cedulas de R$200")
    
    if primeiroValorRestante >= 100:
        cedula100 = primeiroValorRestante // 100
        segundoValorRestante = primeiroValorRestante % 100
        print(f"Total de {cedula100} de R$100")  
        
        if segundoValorRestante >= 50:
            cedula50 = segundoValorRestante // 50
            terceiroValorRestante = segundoValorRestante % 50
            print(f"Total de {cedula50} cedulas de R$50")
            
            if terceiroValorRestante >= 20:
                cedula20 = terceiroValorRestante // 20
                quartoValorRestante = terceiroValorRestante % 20
        
                if quartoValorRestante >= 10:
                    cedula10 = 10 / quartoValorRestante
                    print(f"Total de {cedula10} cedulas de 10")

print("="*30)
print("Python Bank agradece a preferencia!") """               
        
print("="*30)
print("Python Bank")
print("="*30)
saque = int(input("Qual volor de saque? "))
total = saque
cedula = 200
totalCedula = 0

while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f"Total de {totalCedula} cedulas de R${cedula}")
        if cedula == 200:
            cedula = 100
        elif cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0    
        if total == 0:
            break                    


print("="*30)
print("Python Bank agradece a preferencia!")