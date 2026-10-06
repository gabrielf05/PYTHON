# Desafio 66 programa ue leia varios numeors inteiros, para quando digita 999, mostre a qunatidade e a soma desconsiderando o flag
soma = quant = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    soma += n
    quant = quant + 1
print(f'A quantidade de números digitados foi {quant} e a soma de todos eles é {soma}.')