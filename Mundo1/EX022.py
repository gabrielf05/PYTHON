# Desafio 22
# Crie um programa que leia o nome completo de uma pessoa e Mostre:
# - O nome com todas as letras maiusculas
# - O nome com todas minusculas
# - Quantas letras ao todo sem considerar espaços
# - Quantas letras tem o primeiro nome

nome = str(input('Digite o seu nome completo: '))
nome.split()[0]
sem_espaços = nome.replace(' ','')

print('O seu nome com todas as letras maiúsculas fica {}'.format(nome.upper()))
print('O seu nome com todas as letras minúsculas fica {}'.format(nome.lower()))
print(sem_espaços)
print('Seu nome tem {} letras'.format(len(sem_espaços)))
print('O seu primeiro nome tem {} letras'.format(len(nome.split()[0])))