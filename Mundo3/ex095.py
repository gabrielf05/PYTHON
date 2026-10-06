''' Desafio 95 - Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador
'''
dados = {}
gols = []
time = []
while True:
  dados.clear()
  dados['nome'] = str(input('Nome do jogador: '))
  partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
  gols.clear()
  for n in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {n+1}? ')))
  dados['gols'] = gols[:]
  dados['total'] = sum(gols)
  time.append(dados.copy())
  continua = str(input('Quer continua? (S/N) ')).strip().upper()
  while continua not in 'sSnN':
    print('Erro! Responda apenas S ou N.')
    continua = str(input('Quer continuar? (S/N) ')).strip().upper()
  if continua in 'nN':
    break
print('-='*40)
# cabeçalho
print('cod ', end='')
for i in dados.keys():
  print(f'{i:<15}', end='')
print()
print('-='*40)
for k, v in enumerate(time):
  print(f'{k:>3}', end=' ')
  for d in v.values():
    print(f'{str(d):<15}', end=' ')
  print()
print('-='*40)
while True:
  busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
  if busca == 999:
    break
  if busca >= len(time):
    print(f'Erro! Não existe jogador com código {busca}')
  else:
    print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
    for k, v in enumerate(time[busca]['gols']):
      print(f'  No jogo {k+1} fez {v} gols.')
  print('-='*40)
print('<< VOLTE SEMPRE >>')