'''
Desafio 107 - Crie um módulos chamado moeda.py que tenha funções incorporadas, aumentar(), diminuir(), dobro() e metade()
Faça também um programa que importe esse módulo e use algumas funções
'''






p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(p, 13)}')