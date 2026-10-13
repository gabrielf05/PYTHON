'''
Desafio 110 - Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), 
que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
'''
import ex111p.utilidadesCev.Moeda.moeda110 as moeda110


p = float(input('Digite o preço: R$'))
moeda110.resumo(p, 20, 12)