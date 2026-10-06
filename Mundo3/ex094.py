''' Desafio 94 - crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
a) Quantas pessoas foram cadastradas
b) A mpedia de idade do grupo
c) uma lista com todas as mulheres
d) uma lista com todas as pessoas com idade acima da média
'''
dados = {}
lista_tot = []
cont = soma = média = 0
while True:
  dados['nome'] = str(input('Nome: '))
  dados['sexo'] = str(input('Sexo: ')).upper()
  while dados['sexo'] not in 'mMfF':
    print('Erro! Por favor, digite apenas M ou F')
    dados['sexo'] = str(input('Sexo: ')).upper()
  dados['Idade'] = int(input('Idade: '))
  soma += dados['Idade']
  lista_tot.append(dados.copy())
  cont += 1
  continua = str(input('Quer continuar? (S/N) ')).strip().upper()
  while continua not in 'sSnN':
    print('Erro! Responda apenas S ou N.')
    continua = str(input('Quer continuar? (S/N) ')).strip().upper()
  if continua in 'Nn':
    break
print('-='*40)
print(lista_tot)
print(f'A) Ao todo temos {cont} pessoas cadastradas.')
média  = soma / cont
print(f'B) A média de idade do grupo é {média:5.2f} anos.')
print(f'C) As mulheres cadastradas foram', end=' ')
for m in lista_tot:
  if m['sexo'] in 'fF':
    print(f'{m["nome"]}', end=' ')
print()
print(f'D) Lista das pessoas que estão acima da média:')
for n in lista_tot:
  if n['Idade'] > média:
    for k, v in n.items():
      print(f'{k} = {v}', end=' ')
    print()
print('<< ENCERRADO >>')
