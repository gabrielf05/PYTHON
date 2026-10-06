
'''#tuplas, listas e dicionários

#AS TUPLAS SÃO IMUTÁVEIS, NÃO CONSEGUIMOS MUDAR UM PARÂMETRO NO MEIO DO PROGRAMA

lanche = ('hamburguer', 'suco', 'pizza', 'pudim') #(tupla)
print(lanche[0])
print(lanche[1])
print(lanche[2])
print(lanche[3])
print(lanche[0:2])

print(len(lanche))  #vai me dizer quantos itens tem a variável lanche, nesse caso 4

for c in lanche:
  print(c)
'''
'''
lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'Batata frita')
for comida in lanche:
  print(f'Eu vou comer {comida}')

for comida in range(0, len(lanche)):
  print(f'Eu vou comer {lanche[comida]} na posição {comida}')

for pos, comida in enumerate(lanche):
  print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba')
print(sorted(lanche))
'''

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(5)) # quantidade
print(c.index(5)) # posição