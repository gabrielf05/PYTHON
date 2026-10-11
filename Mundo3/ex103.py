'''
Desafio 103 - Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''
'''def ficha(nome=False, gols=0):
    if nome == False:
        Nome = '<desconhecido>'
    else:
        Nome = nome
    print(f'O jogador {Nome} fez', end=' ')
    if gols == 0:
        print(f'0 gol(s) no campeonato')
    else:
        print(f'{gols} gol(s) no campeonato')
'''

def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


Nome = str(input('Nome do jogador: '))
Gols = str(input('Quantos gols o jogador marcou? '))
if Gols.isnumeric():
    Gols = int(Gols)
else:
    Gols = 0

if Nome.strip() == '':
    ficha(gols=Gols)
else:
    ficha(Nome, Gols)