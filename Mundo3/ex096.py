'''
Desafio 96 - Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''
def area(L, c):
  area = L * c
  print(f'A área de um terreno {L}x{c} é {area}m²')


print('  Controle de Terrenos')
print('-' * 24)
L = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(L, c)