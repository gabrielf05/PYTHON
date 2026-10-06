# Desafio 32 leia um ano qualquer e diga se é ano bissexto
import datetime
a = int(input('Que ano quer analisar? Digite 0 para analisar o ano atual: '))
if a == 0:
    a = datetime.date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
  print('O ano {} é Bissexto.'.format(a))
else:
  print('O ano {} não é Bissexto'.format(a))