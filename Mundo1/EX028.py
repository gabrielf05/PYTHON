# Desafio 28
import random
n = int(input('Escolha um número de 0 a 5:'))
Lista = [0,1,2,3,4,5]
num = random.choice(Lista)
print('O número escolhido por você foi {} e pelo computador foi {}'.format(n, num))
if n == num:
  print('Você acertou')
else:
  print('Você errou')