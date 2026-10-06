# Desafio 51 - programa que leia o primeiro termo e a razão de uma PA, mostre os 10 primeiros digitos dessa progressão

termo = int(input('Dgite o primeiro termo da sua PA: '))
razao = int(input('Diigte a razão da sua PA: '))
decimo = termo + (10-1) * razao

'''s = 0
for c in range(1, 11):
  s = termo + (c-1) * razao'''

for c in range(termo, decimo + razao, razao):
  print(c, end=' -> ')

