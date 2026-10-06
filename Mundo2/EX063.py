# Desafio 63 - programa que leia um numero inteiro e mostre os n primeiros elementos de uma sequencia de fibonacci

# A regra de cálculo usa a fórmula algébrica \(F_n = F_{n-1} + F_{n-2}\)
print('-'*30)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*30)
termo = int(input('Quantos termos você quer mostrar: '))
print('-'*30)
primeiro = 0
segundo = 1
c = 1
fib = 0


while c <= termo:
    print('{} - > '.format(primeiro), end='')
    fib = primeiro + segundo
    primeiro = segundo
    segundo = fib
    c = c + 1
print('FIM')
