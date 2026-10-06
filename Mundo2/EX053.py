# Desafio 53 - programa que leia uma frase e diga se ela é um palíndromo

frase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
#print(frase)
contrario = ''
inverso = ''
#print(contrario)
contrario = frase[::-1]
'''for letra in range(len(frase)-1,-1,-1):
  contrario += frase[letra]'''
print('O inverso de {} é {}'.format(frase, contrario))
if frase == contrario:
  print('A frase é um palíndromo')
else:
  print('A frase não é um palíndromo')