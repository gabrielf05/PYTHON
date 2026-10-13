'''
Desafio 112 - Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imput(), mas com uma validação de dados para aceitar apenas valores que seja monetários.
'''
from ex112p.utilidadesCev import Dado
from ex112p.utilidadesCev import Moeda

p = Dado.leiaDinheiro('Digite o preço: R$')
Moeda.resumo(p, 35, 20)
