'''
Desafio 81 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''
lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    continua = str(input('Deseja continuar? (S/N) ')).strip().upper()
    while continua not in 'SN':
        print('opção inválida')
        continua = str(input('Deseja continuar? (S/N) ')).strip().upper()
    if continua in 'Nn':
        break
print('-=' *30)
print(f'Foram digitados {cont} elementos')
print(f'Foram digitados {len(lista)} elementos')
lista.sort(reverse=True)
print(f'A lista ordenada de forma descrescente é {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')