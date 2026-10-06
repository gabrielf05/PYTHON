# Desafio 67 - programa que mostre a tabuada do numero solicitado, o programa é interrompido quando o numero solicitado for negativo

# 1)
while True:
    n = int(input('Digite um número para ver a sua tabuada: '))
    print('-=' * 20)
    if n < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
    x = 1
    while x <= 10:
        print(f'{n} * {x:2} = {n * x}')
        x += 1
    print('-=' * 20)

# 2)
while True:
    n = int(input('Quer ver a tabuada de qual número? '))
    if n < 0:
            break
    print('-' * 20)
    for c in range (1, 11):
        print(f'{n} * {c:2} = {n * c}')
    print('-' * 20)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')