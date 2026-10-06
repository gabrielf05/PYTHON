# Desafio 74
'''
programa que vai gerar cinco números aleatórios e colocar em uma tupla,
depois mostre a listagem de números gerados e também indique o menor e o
maior valor que estão na tupla
'''
import random as r

a = (r.randint(1, 10), r.randint(1, 10), r.randint(1, 10), r.randint(1, 10), r.randint(1, 10))
print(f'A tupla formada por números aleatórios é {a}')
print(f'Os valores sorteados foram: ', end=' ')
for i in a:
  print(f'{i},', end=' ')
print(f'\nO maior valor da tupla é {max(a)}')
print(f'O menor valor da tupla é {min(a)}')