# Desafio 44
print('{:=^40}'.format('LOJAS MORAES'))
produto = float(input('insira o valor do seu produto: '))
print('''Nós temos quatro opções de pagamento:
1 - à vista dinheiro/cheque: 10% de desconto
2 - à vista no cartão: 5% de desconto
3 - em até 2x no cartão: preço formal
4 - 3x ou mais no cartão: 20% de juros''')

opção = int(input(' Qual será a sua forma de pagamento? '))

if opção == 1:
    print('Para pagamentos a vista no dinheiro/cheque o desconto é de 10%, você vai pagar {}'.format(produto * 0.9))
elif opção == 2:
    print('Para pagamentos a vista no cartão o desconto é de 5%, você vai pagar {}'.format(produto * 0.95))
elif opção == 3:
    print('Para pagamentos em até 2x no cartão não oferecemos desconto, você vai pagar {}'.format(produto))
elif opção == 4:
    print('Para pagamentos em 3x ou mais no cartão cobramos uma taxa de 20% no valor do produto, você vai pagar {}'.format(produto * 1.2))