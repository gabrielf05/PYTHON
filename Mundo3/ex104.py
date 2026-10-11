'''
Desafio 104 - Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')
'''
def leiaInt(x):
    while True:
        valor = str(input(x))
        if valor.isnumeric():
            valor = int(valor)
            return valor
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            

# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')