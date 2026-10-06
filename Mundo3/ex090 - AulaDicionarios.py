'''
Dicionários são identificados por {} ou dict()

dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome']) -> Pedro
print(dados['idade']) -> 25

dados['sexo'] = 'M' -> para adicionar elementos ao dicionario
del dados['idade'] -> para deletar elementos do dicionário

filme = {'Título': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
         }

print(filme.values()) -> dict_values(['Star Wars', 1977, 'George Lucas']) - mostra os valores
print(filme.keys()) -> dict_keys(['Título', 'ano', 'diretor']) - mostra as chaves
print(filme.items()) -> dict_items([('Título', 'Star Wars'), ('ano', 1977), ('diretor', 'George Lucas')]) - mostra os itens

for k, v in filme.items():
    print(f'O {k} é {v}')
'''
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
'''print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())'''

'''del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
for k, v in pessoas.items():
  print(f'{k} = {v}')'''

'''estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil = []
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])'''

estado = {}
brasil = []
for c in range(0, 3):
  estado['uf'] = str(input('Unidade Federativa: '))
  estado['sigla'] = str(input('Sigla do Estado: '))
  brasil.append(estado.copy())
for e in brasil:
  for k, v in e.items():
    print(f'O campo {k} tem valor {v}')
