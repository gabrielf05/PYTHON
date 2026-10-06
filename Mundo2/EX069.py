# Desafio 69 - progrma que leia idade e sexo de varias pessoas, a cada pessoa cadastrada deve perguntar se o usuario quer continuar. no final mostre pessoas com mais de 18 anos, quantos homens e qunatas mulheres menos de 20 anos
maiores = homens = novinhas = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: (M/F) ')).strip().upper()[0]
    continua = ' '

# Pergunta se quer continuar cadastrando pessoas

    while continua not in 'SN':
        continua = str(input('Quer continuar? (S/N)')).strip().upper()[0]

# verifica idade

    if idade >= 18:
        maiores += 1

#Verifica sexo

    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        if idade < 20:
            novinhas += 1
    if continua == 'N':
        break

# Resultados

print('-' * 30)
print(f'Total de pessoas com 18 anos ou mais: {maiores}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {novinhas} mulheres com menos de 20 anos')