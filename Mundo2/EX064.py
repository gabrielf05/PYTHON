# Desafio 64 - programa que leia varios numeros inteiros, o programa vai parar quando digitar 999, mostre no final quantos números foram digitados e qual a soma entre eles, desconsiderando o 999

soma = quant = n = 0
while n != 999:
    n = int(input('Digite um valor (999 para parar): '))
    if n != 999:
        quant = quant + 1
        soma = soma + n
print('Você digitou {} números e a soma entre eles foi {}.'.format(quant, soma))