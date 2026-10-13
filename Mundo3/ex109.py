'''
Desafio 109 - Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
'''
import Mundo3.ex111p.utilidadesCev.Moeda.moeda109 as moeda109


p = float(input('Digite o preço: R$'))
forma = str(input('Quer ver este valor formatado? ')).strip().upper()
if forma == 'S':
    forma = True
else:
    forma = False
print(f'A metade de {moeda109.moeda(p)} é {moeda109.metade(p, forma)}')
print(f'O dobro de {moeda109.moeda(p)} é {moeda109.dobro(p, forma)}')
print(f'Aumentando 10%, temos {moeda109.aumentar(p, 10, forma)}')
print(f'Diminuindo 13%, temos {moeda109.diminuir(p, 13, forma)}')