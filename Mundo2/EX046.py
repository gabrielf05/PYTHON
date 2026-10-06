# Desafio 46 - Contagem regressiva de 10 até 0 com um segundo de pausa

import time
print('Contagem regressiva para o estouro de fogos de artifício')
time.sleep(1)
print('-='*15)

for cont in range(10, -1, -1):
  print(cont)
  time.sleep(1)
print('FIM')