'''
o break desvia o caminho para continuação fora da repetição

enquanto Verdadeiro:
    se chão:
        passo
    se buraco:
        pula
    se moeda:
        pega
    se troféu:
        pega
        interrompe
pega

while True:
    if chão:
        passo
    if buraco:
        pula
    if moeda:
        pega
    if troféu:
        pula
        break
pega

'''
# Contagem infinita
'''cont = 1 
while True:
    print(cont, '-> ', end='')
    cont = cont + 1
print('ACABOU')'''

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s = s + n
print('A soma vale {}'.format(s))
print(f'A soma vale {s}')