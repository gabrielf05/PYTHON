'''
Desafio 87 - Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''
soma = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
        matriz[l][c] = num
        if num % 2 == 0:
            soma += num
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[l][c]:^5}', end='')
    print()
print('-='*30)

print(f'A soma dos valores pares é {soma}')
segunda = 0
for p in matriz:
    if p[2] >= segunda:
        segunda = p[1]
print(f'O maior valor da segunda coluna é {segunda}')
terceira = 0
for p in matriz:
    terceira += p[2]
print(f'A soma dos valores da terceira coluna é {terceira}')