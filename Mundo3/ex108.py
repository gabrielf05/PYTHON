'''
Desafio 108 - Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.
'''
import Mundo3.ex111p.utilidadesCev.Moeda.moeda108 as moeda108


p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda108.moeda(p)} é {moeda108.moeda(moeda108.metade(p))}')
print(f'O dobro de {moeda108.moeda(p)} é {moeda108.moeda(moeda108.dobro(p))}')
print(f'Aumentando 10%, temos {moeda108.moeda(moeda108.aumentar(p, 10))}')
print(f'Diminuindo 13%, temos {moeda108.moeda(moeda108.diminuir(p, 13))}')