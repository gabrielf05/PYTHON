''' Desafio 91 - Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
import random
import time
from operator import itemgetter
dado = {}

for n in range(1, 5):
  dado[f'jogador{n}'] = random.randint(1, 6)
print('Valores sorteados:')
for k, v in dado.items():
  print(f'O {k} tirou {v}')
  time.sleep(1)
print()
print('== Ranking dos jogadores ==')
ordenado = list(sorted(dado.items(), key=itemgetter(1), reverse=True))
for k, v in enumerate(ordenado):
  print(f'{k+1}o Lugar: {v[0]} com {v[1]}')
  time.sleep(1)