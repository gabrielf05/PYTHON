'''
Interactive help
help(print)
---------------------------------------------------------------------------
Docstrings - é uma string de documentação (começa log após a função def)
def contador(inicio, fim, passo):
  """
  -> Faz uma contagem e mostra na tela.
  :param inicio: início da contagem
  :param fim: fim da contagem
  :param passo: passo da contagem
  :return: sem retorno
  """
  c = inicio
  while c <= fim:
    print(f'{c}', end='..')
    c += passo
  print('FIM!')

contador(2, 10, 2)
help(contador)
-------------------------------------------------------------------------
Parâmetros opcionais: usando o = 0 no final do parâmetro
def somar(a=0, b=0, c=0):
  s = a + b + c
  print(f'A soma vale {s}')
-------------------------------------------------------------------------
Escopo de variáveis
def teste():
  x = 8
  print(f'Na função teste, n vale {n}')
  print(f'Na função teste, x vale {x}')
-------------------------------------------------------------------------
Retornando valores
def somar(a=0, b=0, c=0):
  s = a + b + c
  return s
-------------------------------------------------------------------------
'''
'''def contador(inicio, fim, passo):
  """
  -> Faz uma contagem e mostra na tela.
  :param inicio: início da contagem
  :param fim: fim da contagem
  :param passo: passo da contagem
  :return: sem retorno
  Função criada por Gabriel Moraes
  """
  c = inicio
  while c <= fim:
    print(f'{c}', end='..')
    c += passo
  print('FIM!')

contador(2, 10, 2)
help(contador)'''

'''def somar(a=0, b=0, c=0):
  """
  -> Faz a soma de três valores e mostra o resultado na tela.
  :param a: primeiro valor
  :param b: segundo valor
  :param c: terceiro valor
  Função criada por Gabriel Moraes
  """
  s = a + b + c
  print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)
somar(c=4, a=5, b=2)'''

'''def teste(b):
  b += 4 # escopo local
  c = 2
  print(f'A dentro vale {a}')
  print(f'B dentro vale {b}')
  print(f'C dentro vale {c}')

a = 5 # escopo global
teste(a)
print(f'A fora vale {a}')
print(f'B fora vale {b}')
print(f'C fora vale {c}')'''

def somar(a=0, b=0, c=0):
  s = a + b + c
  return s

r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Os resultados foram {r1}, {r2} e {r3}')