# Desafio 48 - a soma entre todos os números impares que são múltiplos de 3 entre 1 e 500
cont = 0
s = 0
for c in range(1, 500):
  if c % 3 == 0 and c % 2 != 0:
    s = s + c
    cont = cont + 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, s))
print('FIM')