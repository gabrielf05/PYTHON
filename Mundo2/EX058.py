# Desafio 58 - melhore o jogo do desafio 28 onde o computador vai pensar em um número entre 0 e 10, no final deve mostrar quantos palpites o jogador levou para acertar

# 1)
import random
import time
'''n = int(input('Escolha um número de 0 a 10: '))
Lista = [0,1,2,3,4,5,6,7,8,9,10]
num = random.choice(Lista)
palpites = 0

while n != num:
    print('Você errou')
    print('O número escolhido por você foi {} e pelo computador foi {}'.format(n, num))
    palpites = palpites + 1
    n = int(input('Escolha um número de 0 a 10: '))
    num = random.choice(Lista)
print('Você acertou em {} palpites, o número escolhido por você foi {} e pelo computador foi {}'. format(palpites, n, num))
'''
# 2)

'''num = random.randint(0, 10)
palpites = 1
acertou = False
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
time.sleep(1)
print('Será que você consegue adivinhar qual foi?')
time.sleep(1)

while not acertou:
    n = int(input('Qual é o seu palpite? '))
    if n < num:
        print('Mais... Tente mais uma vez')
        palpites = palpites + 1
    elif n > num:
        print('Menos... Tente mais uma vez')
        palpites = palpites + 1
    elif n == num:
        acertou = True        
print('Você acertou em {} tentativas.'.format(palpites))'''

# 3)

num = random.randint(0, 10)
palpites = 0
acertou = False
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
time.sleep(1)
print('Será que você consegue adivinhar qual foi?')
time.sleep(1)

while not acertou:
    n = int(input('Qual é o seu palpite? '))
    palpites = palpites + 1
    if n == num:
        acertou = True
    else:
        if n < num:
            print('Mais... tente mais uma vez')
        elif n > num:
            print('Menos... Tente mais uma vez')
print('Você acertou em {} tentativas.'.format(palpites))