'''
Desafio 100 - Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''
import random
import time
def sorteia(lista):
    print('Foram sorteados os valores: ', end='')
    for cont in range(0, 5):
        n = random.randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        time.sleep(0.5)
    print('PRONTO!')
    
def somaPar(lista):
    par = 0
    for v in lista:
        if v % 2 == 0:
            par += v
    print(f'A soma dos valores pares é {par}')


numeros = []
sorteia(numeros)
somaPar(numeros)