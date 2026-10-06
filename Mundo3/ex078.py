'''
Desafio 78 - Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''
lista = []
maior = menor = 0
for n in range(0, 5):
    num = int(input(f'Digite um valor para a posição {n}: '))
    lista.append(num)
    if n == 0:
        maior = num
        menor = num
    else:
        if maior < num :
            maior = num
        if menor > num :
            menor = num
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')

for pos, valor in enumerate(lista):
    if valor == maior:
        print(f'{pos}...', end=' ')
        
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for pos, valor in enumerate(lista):   
    if valor == menor:
        print(f'{pos}...', end=' ')