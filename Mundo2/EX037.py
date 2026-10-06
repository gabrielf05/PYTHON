# Desafio 37
'''Ler um número interiro e pedir para converter para binário, octal ou hexadecimal'''

n = int(input('Digite um número inteiro: '))
print('Escolha uma opção de conversão: ')
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
opção = int(input('Digite a opção desejada:'))

if opção == 1:
    print('O número {} convertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:])) # [2:] serve para remover o prefixo '0b' que indica que é binário
elif opção == 2:
    print('O número {} convertido para OCTAL é igual a {}'.format(n,oct(n)[2:])) # [2:] serve para remover o prefixo '0o' que indica que é octal
elif opção == 3:
    print('O número {} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:])) # [2:] serve para remover o prefixo '0x' que indica que é hexadecimal
else:
    print('Opção inválida! Tente novamente.')

