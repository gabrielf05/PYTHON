'''
Desafio 79 - Faça um programa que leia vários números e coloque-os em uma lista. Depois disso, mostre:
todos os valores únicos digitados, em ordem crescente.
''' 
lista = []
while True:
    num = int(input('Digite um valor: '))
    if num in lista:
        print('Valor duplicado! Não vou adicionar')
    else:
        lista.append(num)
        print('Valor adicionado com sucesso...')
    continua = str(input('Quer continuar? (S/N) ')).strip().upper()
    while continua not in 'SN':
        print('Opção inválida.')
        continua = str(input('Quer continuar? (S/N) ')).strip().upper()
    if continua == 'N':
        break
    print('-='*30)
print('-='*30)
lista.sort()
print(f'Você digitou os valores {lista}')