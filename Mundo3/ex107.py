'''
Desafio 107 - Crie um módulos chamado moeda.py que tenha funções incorporadas, aumentar(), diminuir(), dobro() e metade()
Faça também um programa que importe esse módulo e use algumas funções
'''
import Mundo3.ex111p.utilidadesCev.Moeda.moeda107 as moeda107


p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é R${moeda107.metade(p)}')
print(f'O dobro de R${p} é R${moeda107.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda107.aumentar(p, 10)}')
print(f'Diminuindo 13%, temos R${moeda107.diminuir(p, 13)}')