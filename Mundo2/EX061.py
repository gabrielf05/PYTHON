# Desafio 61 - refaça o desafio 51 usando uma estrutura while
'''
termo = int(input('Dgite o primeiro termo da sua PA: '))
razao = int(input('Diigte a razão da sua PA: '))
decimo = termo + (10-1) * razao
c = termo

while c < decimo + razao:
  print(c, end=' -> ')
  c = c + razao
print("FIM")'''

termo = int(input('Dgite o primeiro termo da sua PA: '))
razao = int(input('Diigte a razão da sua PA: '))
primeiro = termo
c = 1

while c <= 10:
  print('{} - > '.format(primeiro), end='')
  primeiro = primeiro + razao
  c = c + 1
print('FIM')

# Desafio 51 - programa que leia o primeiro termo e a razão de uma PA, mostre os 10 primeiros digitos dessa progressão
'''
termo = int(input('Dgite o primeiro termo da sua PA: '))
razao = int(input('Diigte a razão da sua PA: '))
decimo = termo + (10-1) * razao

s = 0
for c in range(1, 11):
  s = termo + (c-1) * razao

for c in range(termo, decimo + razao, razao):
  print(c, end=' -> ')'''

