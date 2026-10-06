# Desafio 24
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'
cidade = str(input('Digite o nome da sua cidade: '))
começo = cidade.split()[0]
print('SANTO' in começo.upper())
print(começo)