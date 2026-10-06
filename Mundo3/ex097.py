'''
Desafio 97 - Faça um programa que tenha a função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
'''
def escreva(msg):
  tam = len(msg) + 4
  print('~' * tam)
  print(f'  {msg}')
  print('~' * tam)


frase = str(input('Digite uma frase: '))
escreva(frase)