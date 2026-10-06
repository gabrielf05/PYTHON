# Desafio 41

import datetime
ano = int(input('Qual seu ano de nascimento? '))
idade = (datetime.date.today().year) - ano

if idade <= 9:
    print('O atleta tem {} anos, ele está na categoria MIRIM'.format(idade))
elif 9 < idade <= 14:
    print('O atleta tem {} anos, ele está na categoria INFANTIL'.format(idade))
elif 14 < idade <= 19:
     print('O atleta tem {} anos, ele está na categoria JÚNIOR'.format(idade))
elif 19 < idade <= 25:
     print('O atleta tem {} anos, ele está na categoria SÊNIOR'.format(idade))
else:
      print('O atleta tem {} anos, ele está na categoria MASTER'.format(idade))