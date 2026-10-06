# Desafio 60 - programa que leia um número qualquer e mostre seu fatorial
import math
n = int(input('Digite um número para ver o seu fatorial: '))
f = 1
c = n
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print('{}'.format(f))

'''for c in range(c, 1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print('{}'.format(f))'''