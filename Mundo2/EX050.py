# Desafio 50 - programa que leia 6 números e mostre a soma apenas dos pares
s = 0
cont = 0
for c in range(0, 6):
  n = int(input('Digite um número: '))
  if n % 2 == 0:
    s = s + n
    cont = cont + 1
print('Você informou {} números pares e a soma foi {}'.format(cont, s))
print('FIM')


