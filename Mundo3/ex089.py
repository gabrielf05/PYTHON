'''
Desafio 89 - Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''
turma = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: ' ))
    n2 = float(input('Nota 2: ' ))
    media = (n1 + n2) / 2
    turma.append([nome, [n1, n2], media])
    continua = str(input('Quer continua? (S/N) ')).strip().upper()
    if continua == 'N':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for pos, n in enumerate(turma):
    print(f'{pos:<4} {n[0]:<10} {n[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(turma) - 1:
        print(f'Notas de {turma[opc][0]} são {turma[opc][1]}')
        