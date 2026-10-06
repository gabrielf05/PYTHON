# Desafio 55 - programa que leia o peso de 5 pessoas e mostre o maior e o menor
maior = 0
menor = 0
for c in range(1,6):
  peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
  if c == 1: # este valor é o menor e o maior no momento
    maior = peso
    menor = peso
  if maior < peso:
    maior = peso
  elif menor > peso:
    menor = peso
print('O maior peso lido foi {}Kg'.format(maior))
print('O menor peso lido foi {}Kg'.format(menor))

'''peso = []
for c in range(0,5):
  peso.append(float(input('Digite o seu peso: '))) #append adiciona o elemento ao fina da lista peso
print(max(peso))
print(min(peso))'''



#maior = max(peso)
#menor = min(peso)
#if peso > peso:
#  maior = peso
#else:
#  menor = peso
#print('O maior peso lido foi de {}Kg'.format(maior))
#print('O menor peso lido foi de {}Kg'.format(menor))

#print('O maior peso lido foi de {}Kg'.format())
#print('O menor peso lido foi de {}Kg'.format())