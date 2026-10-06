'''
lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
lanche[3] = 'picolé'

Listas podem ser modificadas

lanche.append[cookie] adiciona no fim da lista
lanche.insert[0, 'cachorro quente'] insere irem no local 0
del lanche[3]
lanche.pop(3) sem o indice, elimina o ultimo item
lanche.remove('pizza)

if pizza in lanche:
    lanche.remove('pizza')
    
valores = list(range(4, 11))
valores = [4, 5, 6, 7, 8, 9, 10]

.sort - Ordena os números da lista
.sort(reverse=True) - Ordem reversa
len(valores) = 7
'''
'''
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
#num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos')'''

valores = []
#valores.append(5)
#valores.append(9)
#valores.append(4)
'''for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores): #enumerate pega tanto a posição, quanto o valor
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')'''

a = [2, 3, 4, 7]
b = a [:] # cria uma cópia de a em b
b[2] = 8 # a partir do momento que iguala as listas cria uma conexão
print(f'Lista A {a}')
print(f'Lista B {b}')