'''
print('-------------------------')
print('    SISTEMA DE ALUNOS    ')
print('-------------------------')
print('-------------------------')
print('CADASTRO DE FUNCIONÁRIOS ')
print('-------------------------')
print('-------------------------')
print('     ERRO DO SISTEMA     ')
print('-------------------------')

def mostralinha():
  print('-------------------------')

mostralinha()
print('    SISTEMA DE ALUNOS    ')
mostralinha()
mostralinha()
print('CADASTRO DE FUNCIONÁRIOS ')
mostralinha()
mostralinha()
print('     ERRO DO SISTEMA     ')
mostralinha()

def mensagem(msg):
  print('-------------------------')
  print(msg)
  print('-------------------------')

mensagem('SISTEMA DE ALUNOS')
mensagem('CADASTRO DE FUNCIONÁRIOS')
mensagem('ERRO DO SISTEMA')
'''

def soma(a, b):
  s = a + b
  print(s)


soma(4, 5)
soma(8, 9)
soma(2, 1)

# DESEMPACOTAR
def contador(*num):
  print(num)

contador(2, 1, 7)
contador(8, 0)
contador()

def contador(*num):
  tam = len(num)
  print(f'Recebi os valores {num} e são ao todo {tam} números')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def dobra(lst):
  pos = 0
  while pos < len(lst):
    lst[pos] *= 2
    pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)