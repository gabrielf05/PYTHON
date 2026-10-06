# Desafio 73
'''
 crie um tupla com os 20 prmeiros colocados do brasileirão, ordem de colocação.
 moste apenas os cinco primeiros colocados
 mostre os últimos quatro colocados
 uma lista com os times em ordem alfabética
 em que posição está o time do são paulo
'''
a = ('Flamengo', 'Palmeiras', 'Athletico-PR', 'Bahia', 'Fluminense', 'Cruzeiro',
'Atlético-MG', 'Coritiba', 'Bragantino', 'Santos', 'São Paulo', 'EC Vitória',
'Corinthians', 'Botafogo', 'Mirassol', 'Grêmio', 'Vasco da Gama', 'Internacional',
'Remo', 'Chapecoense')

#escolha = int(input('Escolha uma das opções abaixo: '))
#if escolha == 1:
print('-='*50)
print(f'Os primeiros cinco colocados são {a[0:5]}')
#elif escolha == 2:
print('-='*50)
print(f'Os quatro últimos colocados são {a[16:]}')
#elif escolha == 3:
print('-='*50)
print(f'Times em ordem alfabética: {sorted(a)}')
#elif escolha == 4:
print('-='*50)
print(f'A Chapecoense está na {a.index('Chapecoense')+1}ª posição')
