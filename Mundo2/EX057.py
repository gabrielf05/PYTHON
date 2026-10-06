# Desafio 57 - programa que leia o sexo de uma pessoa, ams só aceite M ou F, se estiver errado peça a digitação correta

# 1)
s = ''
while s != 'F' and s != 'M':
    s = str(input('Digite o seu sexo (F/M): ')).upper()
    if s != 'F' and s != 'M':    
        print('Dados inválidos, informe um valor correto para o seu sexo.')
print('Sexo {} registrado com sucesso'.format(s))


# 2)
sexo = str(input('Informe o seu sexo (M/F): ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dasos inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))