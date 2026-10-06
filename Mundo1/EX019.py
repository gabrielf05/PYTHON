import random

a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
a5 = input('Digite o nome do quinto aluno: ')
a6 = input('Digite o nome do sexto aluno: ')

lista = [a1,a2,a3,a4,a5,a6] #no python uma lista fica sempre entre colchetes
escolha = random.choice(lista)
print('O aluno(a) escolhido foi {}.'.formact(escolha))