''' Desafio 93 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
o aproveitamento será uma lista
'''
dados = {}
gols = []
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for n in range(0, partidas):
  gols.append(int(input(f'Quantos gols na partida {n+1}?')))
dados['gols'] = gols[:]
dados['total'] = sum(gols)
print('-='*40)
print(dados)
print('-='*40)
for k, v in dados.items():
  print(f'O campo {k} tem valor {v}')
print('-='*40)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas')
for k, v in enumerate(gols):
  print(f'  => Na partida {k+1}, fez {v} gols.')
print(f'foi um total de {dados["total"]} gols')
