# Desafio 52 - programa que leia um numero inteiro e diga se ele é primo
n = int(input('Digite um número: '))
primo = tal = 0
for c in range(1, n + 1):
  if n % c == 0:
    print('\033[33m', end=' ')
    primo = primo + 1
  else:
    print('\033[31m', end=' ')
    tal += 1
  print('{}'.format(c), end=' ')
print('\n\033[O número {} foi divisível {} vezes'.format(n, primo))
if primo == 2:
  print('E por isso ele é PRIMO!')
else:
  print('E por isso ele NÃO é PRIMO')