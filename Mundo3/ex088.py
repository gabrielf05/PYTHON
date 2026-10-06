'''
Desafio 88 - Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
No final, mostre os palpites gerados na tela.
'''
import random
import time

print('-' * 40)
print('{:^40}'.format ('JOGA NA MEGA SENA'))
print('-' * 40)

jogos = []
num = int(input('Quantos jogos você quer eu eu sorteie? '))
print('-' * 40)

for n in range(1, num+1):
    palpite = []
    while len(palpite) < 6:
        numero = random.randint(1, 60)
        if numero not in palpite:
            palpite.append(numero)
    palpite.sort()
    jogos.append(palpite[:])
print('SORTEANDO OS JOGOS...')
for n in range(len(jogos)):
    print(f'jogo {n+1}: {jogos[n]}')
    time.sleep(1)
    