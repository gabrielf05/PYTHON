# Desafio 54 - programa que leia o ano de nascimento de 7 pessoas e diga quantas atingiram a maioridade, 21 anos
import datetime

'''n1 = int(input('Insira seu ano de nascimento: '))
n2 = int(input('Insira seu ano de nascimento: '))
n3 = int(input('Insira seu ano de nascimento: '))
n4 = int(input('Insira seu ano de nascimento: '))
n5 = int(input('Insira seu ano de nascimento: '))
n6 = int(input('Insira seu ano de nascimento: '))
n7 = int(input('Insira seu ano de nascimento: '))'''

maior = 0
menor = 0
for pessoas in range(1,8):
  n = int(input('Insira seu ano de nascimento: '))
  idade = datetime.date.today().year - n
  if idade >= 21:
    maior = maior + 1
  elif idade < 21:
    menor = menor + 1
print('Das 7 pessoas do grupo, {} já atingiram a maioridade e {} ainda não.'.format(maior, menor))

for pessoas in range(1,8):
  n = int(input('Insira seu ano de nascimento: '))
  idade = datetime.date.today().year - n
  if idade >= 21:
    maior = maior + 1
  else:
    menor = menor + 1
print('Das 7 pessoas do grupo, {} já atingiram a maioridade e {} ainda não.'.format(maior, menor))