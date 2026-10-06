# Desafio 72
# crie um programa que tenha uma tupla por extenso de 0 a 20, o programa deverá ler um número pelo teclado e mostrar por extenso
a = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
     'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
     'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
  num = int(input('Digite um número de 0 a 20: '))
  if 0 <= num <= 20:
    print(f'Você digitou o número {a[num]}')
    continua = str(input('Você quer digitar um novo número? (S/N) ')).strip().upper()
    if continua == 'N':
      break
  else:
    print('Tente novamente. ')

# alterar para perguntar se o usuário quer continuar