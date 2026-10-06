# Desafio 75
'''
Deselvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

Quantas vezes apareceu o valor 9.
Em que posição foi digitado o primeiro valor 3.
Quais foram os números pares.
'''

a = (int(input('Digite um valor:')), int(input('Digite um valor:')), int(input('Digite um valor:')), int(input('Digite um valor:')))
print(f'O valor 9 apareceu {a.count(9)} vezes')
if 3 not in a:
  print('O valor 3 não foi digitado em nenhuma posição')
else:
  print(f'O primeiro valor 3 apareceu na {a.index(3)+1}ª posição')


print(f'Os números pares são', end=' ')
for n in a:
  if n % 2 == 0:
    print(n, end=' ')