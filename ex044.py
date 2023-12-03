"""Elabore uma aplicacao que calcule o valor a ser pago por um produto,
considerando seu preco normal e condicao de pagamento:
-a vista dinheiro/cheque:10% de desconto
-a vista no cartao:5% de desconto
-em ate duas vezes no cartao:preco normal
-3x ou mais no cartao: 20% de juros
"""



produto_preco = float(input("Digite o valor do produto: "))

print("R${:.2f} ".format(produto_preco))

desconto_dinheiro_cheque_a_vista = produto_preco - (produto_preco * 10) / 100

desconto_a_vista_cartao = produto_preco - (produto_preco * 5) / 100

parcelamento_cartao_duasx = produto_preco

parcelamento_cartao_3xoumais = produto_preco + (produto_preco * 20) / 100

print("Escolha o numero da opcao de pagamento: ")
print('-=-=-=-= ' * 5)
print('[1] Pagamento a vista dinheiro ou cheque.')
print('[2] Pagamento a vista no cartao.')
print('[3] Pagamento parcelado em 2x.')
print('[4] Pagamento parcelado 3 ou + vezes')
print('[x] Sair')

OpcaoDePagamento = str(input("Digite a opcao de pagamento: "))

if OpcaoDePagamento == "1":
    print("O produto adquirido custa R${:.2f} com desconto da opcao de pagamento passara a custar R${:.2f} ".format(produto_preco, desconto_dinheiro_cheque_a_vista))
        
elif OpcaoDePagamento == "2":
    print("O produto adquirido custa R${:.2f} com desconto da opcao de pagamento passara a custar R$ R${:.2f} ".format(produto_preco, desconto_a_vista_cartao))
        
elif OpcaoDePagamento == "3":
    print("preco do produto nessa opcao de pagamento e de R${:.2f} ".format(parcelamento_cartao_duasx))
      
elif OpcaoDePagamento == "4":
    print("Esta opcao de pagamento possui 20 porcento de juros e passara a custar R${:.2f} ".format(parcelamento_cartao_3xoumais))
      
elif OpcaoDePagamento == "x" or "X":
    print()
  