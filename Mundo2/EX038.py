# Desafio 38
'''Ler 2 valores e printar o primeiro valor é maior o segundo é maior ou os dois são iguais
'''
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

if n1 > n2:
    print('O primeiro valor é o maior.')
elif n2 > n1 :
    print('O segundo valor é o maior.')
else:
    print('não existe valor maior, os dois são iguais.')