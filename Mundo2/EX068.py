# Desafio 68 - programa que jogue par ou impar, o jogo é interrompido quando o jogador perder, mostrando o total de vitprias consecutivas que ele conseguiu, você deve escolher par ou impar
import random
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
cont = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = random.randint(0, 10)
    soma = jogador + computador
    x = str(input('Par ou ímpar? (P/I) ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}. ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if x == 'P':
        if soma % 2 == 0:
            print('-'*30)
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    elif x == 'I':
        if soma % 2 == 1:
            print('-'*30)
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {cont} vezes')