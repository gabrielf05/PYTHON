# Desafio 49 - Tabuada do desafio 9 utilizando laço for
''' # Desafio 9

x = int(input('Digite um número para ver a sua tabuada:'))
x1 = x*1
x2 = x*2
x3 = x*3
x4 = x*4
x5 = x*5
x6 = x*6
x7 = x*7
x8 = x*8
x9 = x*9
x10 = x*10
#print('A tabuada de {} é \n{}*1 = {}\n{}*2 = {}\n{}*3 = {}\n{}*4 = {}\n{}*5 = {}\n{}*6 = {}\n{}*7 = {}\n{}*8 = {}\n{}*9 = {}\n{}*10 = {}'.format(x,x,x1,x,x2,x,x3,x,x4,x,x5,x,x6,x,x7,x,x8,x,x9,x,x10))
print('{} x {:2} = {}'.format(x,1,x*1))
print('{} x {:2} = {}'.format(x,2,x*2))
print('{} x {:2} = {}'.format(x,3,x*3))
print('{} x {:2} = {}'.format(x,4,x*4))
print('{} x {:2} = {}'.format(x,5,x*5))
print('{} x {:2} = {}'.format(x,6,x*6))
print('{} x {:2} = {}'.format(x,7,x*7))
print('{} x {:2} = {}'.format(x,8,x*8))
print('{} x {:2} = {}'.format(x,9,x*9))
print('{} x {:2} = {}'.format(x,10,x*10))'''

x = int(input('Digite um número para ver a sua tabuada: '))
print('-='*20)
print('A tabuada do {} é: '.format(x))
for c in range(0, 11):
  print('{} x {:2} = {}'.format(x, c, x*c))