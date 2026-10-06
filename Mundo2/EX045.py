# Desafio 45

import random
import time

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = random.randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')

opção = int(input('Qual a sua jogada? '))
print('-='*30)

print('JÓ')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ')
time.sleep(1)

print('-='*30)

print('''O computador escolheu {}
Você escolheu {}'''.format(itens[computador], itens[opção]))

print('-='*30)

'''if computador == 0 and opção == 0 or computador == 1 and opção == 1 or computador == 2 and opção == 2:
    print('Neste caso foi empate')
elif computador == 0 and opção == 2 or computador == 1 and opção == 0 or computador == 2 and opção == 1:
    print('Neste caso você perdeu')
elif computador == 0 and opção == 1 or computador == 1 and opção == 2 or computador == 2 and opção == 0:
    print('Parabéns, você venceu')'''

if computador == 0:
    if opção == 0:
        print('EMPATE')
    elif opção == 1:
        print('JOGADOR VENCE')
    elif opção == 2:
        print('COMPUTADOR VENCE')
elif computador == 1:
    if opção == 0:
        print('COMPUTADOR VENCE')
    elif opção == 1:
        print('EMPATE')
    elif opção == 2:
        print('JOGADOR VENCE')
elif computador == 2:
    if opção == 0:
        print('JOGADOR VENCE')
    elif opção == 1:
        print('COMPUTADOR VENCE')
    elif opção == 2:
        print('EMPATE')