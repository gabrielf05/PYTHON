'''
dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0]) -> Pedro
print(dados[1]) -> 25

pessoas = list()
pessoas.append(dados[:]) - coloca a lista dados dentro de um elemento da lista pessoas
print(pessoas[0]) -> Pedro, 25

pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]] - 3 listas dentro da lista pessoas
print(pessoas[0][0]) -> Pedro
print(pessoas[1][1]) -> 19
print(pessoas[2][0]) -> João
print(pessoas[1]) -> ['Maria', 19]
'''
'''
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:]) # Cria uma cópia sem vincular as duas listas
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
'''
'''
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
'''
galera = []
dado = []
maior = menor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
    
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menor += 1
print(f'Temos {maior} maiores e {menor} menores da idade')