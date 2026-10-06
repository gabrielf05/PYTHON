'''
Desafio 84 - Crie um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
temp = []
lista = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] >= maior:
            maior = temp[1]
        elif temp[1] <= menor:
            menor = temp[1]
    lista.append(temp[:])
    temp.clear()
    continua = str(input('Quer continuar? (S/N) ')).strip().upper()
    while continua not in 'sSnN':
        continua = str(input('Quer continuar? (S/N) ')).strip().upper()
    if continua in 'nN':
        break
print(f'Ao todo, você cadastrou {len(lista)} pessoas.')
print(f'o maior peso foi {maior} de ', end='')
for mai in lista:
    if mai[1] == maior:
        print(f'[{mai[0]}]', end=' ')
print()
print(f'o menor peso foi {menor} de', end='')
for men in lista:
    if men[1] == menor:
        print(f'[{men[0]}]', end=' ')
        
    
