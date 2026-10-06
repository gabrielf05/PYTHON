'''
Usa o for quando se sabe o range das repetições
while se usa quando você não tem o range das repetições

Enquanto não maçã:
    passo
pega

while not maçã:
    passo
pega

While not maçã:
    if chão == sim:
        ande para frente
    if buraco == sim:
        pule o  buraco
    if moeda == sim:
        pega moeda
pega maçã
'''

'''for c in range(1, 10):
    print(c)

c = 1
while c < 10:
    print(c)
    c = c + 1
print('FIM')


n = 1
while n != 0: # Condição de parada
    n = (int(input('Digite um valor: ')))
print('FIM')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar (S/N)')).upper()
print('FIM')'''

n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print('A quantidade de valor pares foi {}'.format(par))
print('A quantidade de valores impares foi {}'.format(impar))
print('ACABOU')