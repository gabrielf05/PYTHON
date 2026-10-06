# desafio 59 - programa que leia dois valores e mostre um menu pergiuntando qual operação fazer, somar, multiplicar, maior, novos números e sair do programa

import time
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
opção = 0
num = 0
while opção != 5:
    print('O que você quer fazer com eles? \n' \
    '[1] Somar \n' \
    '[2] Multiplicar \n' \
    '[3] Maior \n' \
    '[4] Novos números \n' \
    '[5] Sair do programa')
    opção = int(input('Escolha uma das opções acima: '))
    if opção == 1:
        num = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, num))
    elif opção == 2:
        num = n1 * n2
        print('A multiuplicação entre {} e {} é {}'.format(n1, n2, num))
    elif opção == 3:
        if n1 > n2:
            print('O número {} é maior que o {}'.format(n1, n2))
        elif n1 < n2:
            print('O número {} é menor que o {}'.format(n1, n2))
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print("Opção inválida, tente novamente!")
    print('-=' * 10)
    time.sleep(2)
print('Fim do programa, volte sempre!')

