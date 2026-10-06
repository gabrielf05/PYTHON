# Desafio 70 - programa que leia nome e preço do produto, perguntar e quer continuar, total gasto na compra, quantos produtos custam mais de 1000 e qual o produto mais barato
print('-' * 40)
print('{:^40}'.format('LOJAS MORAES DELAS'))
print('-' * 40)
soma = maismil = barato = 0
pbarato = ' '
while True:
    produto = str(input('Informe o nome do produto: '))
    valor = float(input('Informe o preço do produto: '))
    barato = valor
    pbarato = produto
    if valor < barato:
        barato = valor
        pbarato = produto
    continua = ' '
    soma = soma + valor
    while continua not in 'SN':
        continua = str(input('Deseja informar outro produto? (S/N) ')).strip().upper()[0]
    if valor > 1000:
        maismil += 1
    if continua == 'N':
        break
print(f'O valor total da compra foi R${soma:.2f}')
print(f'Temos {maismil} produtos custando mais de R$ 1.000,00')
print(f'O produto mais barato foi {pbarato} que custa R${barato:.2f}')