#Desafio 56 - programa que leia nome, idade e sexo de cada pessoa, deve mostrar a média de idade do grupo, o nome do homem mais velho e quantas mulheres tem menos de 20 anos

velho = 0
novinhas = 0
média = 0
nomevelho = ''

for c in range(1,5):
  print('----- {}ª pessoa ------'.format(c))
  nome = str(input('Digite o seu nome: ')).strip()
  idade = int(input('Digite a sua idade: '))
  sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()
  média = média + idade
  if c == 1 and sexo == 'M':
    velho = idade
    nomevelho = nome
  if velho < idade and sexo == 'M':
    velho = idade
    nomevelho = nome
  if sexo == 'F' and idade < 20:
    novinhas = novinhas + 1

média = média / 4

print('A média de idade do grupo é de {} anos'.format(média))
print('O homem mais velho tem {} anos e seu nome é {}. '.format(velho, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(novinhas))
