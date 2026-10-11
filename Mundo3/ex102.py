'''
Desafio 102 - Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show,
que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial
'''

def fatorial(num, show=False):
  """
  -> Calcula o Fatorial de um número.
  :param num: O número a ser calculado.
  :param show: (opcional) Mostrar ou não a conta.
  :return: O valor do Fatorial de um número num.
  """
  f = 1
  print(f'O fatorial de {num} é:', end=' ')
  for n in range(num, 0, -1):
    if show:
      print(f'{n}', end=' ')
      if n > 1:
        print('X', end=' ')
      else:
        print('=', end=' ')
    f *= n
  return f

numero = int(input('Digite um número para calcular seu fatorial: '))
mostrar = str(input('Deseja mostrar o cálculo? (S/N) ')).strip().upper()
if mostrar == 'S':
  mostrar = True
else:
  mostrar = False
print(fatorial(numero, mostrar))
