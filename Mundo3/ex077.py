# Desafio 77
'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''
lista = ('aprender', 'programar', 'linguagem', 'python', 'curso',
         'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
         'programador', 'futuro', 'faculdade', 'gringa')

for n in lista:
    print(f'\nNa palavra {n.upper()} temos as seguintes vogais: ', end=' ')
    for letra in n:
      if letra.lower() in 'aeiou':
        print(letra.upper(), end=' ')
