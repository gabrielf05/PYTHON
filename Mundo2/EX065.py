# Desafio 65 - programa que leia varios numeros inteiros e mostre a media entre todos e qual foi o maior e o menor, pergunte sempre se o usuário quer continuar a digitar valores
continua = 's'
media = cont = soma = maior = menor = 0

while continua in 'sS':
    n = int(input('Digite um número: '))
    continua = str(input('Quer continuar (S/N)? ')).strip().upper()[0]
    cont = cont + 1
    soma = soma + n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

media = soma / cont
print('Você digitou {} números e a média foi {:.2f}'.format(cont, media))
print('O menor número digitado foi {} e o maior foi {}.'.format(menor, maior))