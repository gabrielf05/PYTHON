#fl4rX+NWZG2T7P1gYLRhPOVUwoEHn1bBbPjh9w1JspA=

''' Laços de repetição
laço c no intervalo(1,0):
  passo
pega

for c in range(1,0):
  passo
pega

for c in range(0,3):
  passo
  pula
passo
pega

for c in range(0,3):
  if moeda:
    pega
  else:
  passo
  pula
passo
pega '''

import time

'''for c in range(6,-1,-1):
  print(c)
  time.sleep(1)
print('FIM')'''

'''n = int(input('Digite um número: '))
for c in range(0, n+1):
  print(c)
print('FIM')'''

s = 0
for c in range(0, 3):
  n = int(input('Digite um valor: '))
  s = s + n
print('O somat´rio de todos os valores foi {}'.format(s))

# ACUMULADOR SOMA UM VALOR
# CONTADOR NORMALMENTE SOMA 1
