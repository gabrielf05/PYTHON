'''
Desafio 80 - Faça um programa que leia 5 valores e coloque-os em uma lista já na posição correta sem utilizar o sort(). No final, mostre a lista ordenada de forma crescente.

'''
lista = []
for n in range(0, 5):
    num = int(input('Digite um valor: '))
    if n == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista')
    else:
        for pos in range(len(lista)): # usado para percorrer as posições da lista
            if num <= lista[pos]: # compara o número digitado com o valor da lista em cada posição
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista')
                break
print(f'Os valores digitados em ordem foram {lista}')