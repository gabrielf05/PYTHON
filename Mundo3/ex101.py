'''
Desafio 101 - Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
'''
import datetime
def voto(ano):
  idade = datetime.date.today().year - ano
  if idade < 16:
    print(f'Com {idade} anos, o candidato ainda não pode votar')
  elif 16 <= idade < 18 or idade > 65:
    print(f'Com {idade} anos, o candidato tem o voto opcional')
  else:
    print(f'Com {idade} anos, o candidato tem o voto obrigatório')



nascimento = int(input('Insira o ano do seu nascimento: '))
voto(nascimento)