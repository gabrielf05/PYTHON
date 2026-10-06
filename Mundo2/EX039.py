# Desafio 39
import datetime

ano = int(input('Qual o seu ano de nescimento? '))
idade = (datetime.date.today().year - ano)
alistamento = (18 - idade)

if idade < 18:
    print('Quem nasceu em {} tem {} anos, faltam {} anos para você se alistar.'.format(ano, idade, alistamento))
elif idade == 18:
    print('Quem nasceu em {} tem {} anos, está na hora de vocês se alistar!'.format(ano, idade))
else:
    print('Quem nasceu em {} tem {} anos, já passou do prazo para você se alistar.'.format(ano, idade))