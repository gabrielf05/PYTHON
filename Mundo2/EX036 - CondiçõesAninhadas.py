'''
Condições Aninhadas
if carro.esquerda(): # atua um ou outro bloco dependendo da condição
  Bloco True
elif carro.direita():
    Bloco True
else:
  Bloco False
'''

nome= str(input('Qual é o seu nome: '))
if nome == 'Gabriel':
    print('Que nome lindo você tem.')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Clara Beatriz Sofia':
    print('Belo nome feminino você tem.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
