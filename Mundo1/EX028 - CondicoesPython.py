#if carro.esquerda(): # atua um ou outro bloco dependendo da condição
#  Bloco True
#else:
#  Bloco False

tempo = int(input('Quantoas anos tem seu carro? '))
#if tempo <=3:
#  print('Carro novo')
#else:
#  print('Carro antigo')

print('carro novo' if tempo<=3 else 'carro antigo')
print('--FIM--')



nome = str(input('Qual o seu nome? ')).strip()
if nome == 'Gabriel':
  print('Que nome lindo você tem.')
else:
  print('Seu nome é tão normal')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.2f}'.format(m))
if m >= 6:
  print('Parabéns, você foi aprovado!')
else:
  print('Infelizmente você foi reprovado')