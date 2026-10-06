''' Desafio 92 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente além da idade
com quantoas anos a pessoa vai se aposentar - 35 anos de contribuição para aposentar
'''
import datetime

dados = {}
dados['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.date.today().year - nascimento
dados['CTPS'] = int(input('Número da carteira de Trabalho (0 não tem): '))
if dados['CTPS'] != 0:
  dados['Contratação'] = int(input('Ano de contratação: '))
  dados['Salário'] = float(input('Salário: R$ '))
  dados['Aposentadoria'] = (dados['Contratação'] - nascimento) + 35
print('-='*40)
for k, v in dados.items():
  print(f'{k} tem o valor {v}')