'''
Desafio 82 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''
lista = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    continua = str(input('Deseja continuar? (S/N) ')).strip().upper()
    while continua not in 'SN':
        print('Opção inválida. Tente novamente...')
        continua = str(input('Deseja continuar? (S/N) ')).strip().upper()
    if continua == 'N':
        break

par = []
impar = []
for valor in lista:
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print('-='*30)
print(f'A lista principal é {lista}')
print(f'A lista com os valores pares é {par}')
print(f'A lista com os valores ímpares é {impar}')