# Desafio 76
'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

a = ('Lápis', 1.50, 'Caderno', 20.00,
     'Mochila', 199.99, 'Caneta', 3.00,
     'Lapiseira', 25.00, 'compasso', 9.99,
     'Transferidor', 4.20)
print('-'*40)
print('LISTAGEM DE PREÇOS')
print('-'*40)

for pos in range(0, len(a)):
  if pos % 2 == 0:
    print(f'{a[pos]:.<30}', end='')
  elif pos % 2 == 1:
    print(f'R$ {a[pos]:>6}')
print('-'*40)