# Fatiamento (pegar pedaços da string)
frase = 'Curso em Vídeo Python'
print(frase[9]) # vai mostrar apenas a str 9
print(frase[9:21]) # vai mostrar da str 9 até 20, sempre um abaixo do final
print(frase[9:21:2]) # vai mostrar da str 9 até 20, pulando de 2 em 2
print(frase[:5]) # = a frase[0:5]
print(frase[15:]) # = a frase[15:21]
print(frase[9::3]) # vai mostrar da str 9 até 20, pulando de 3 em 3

# Análise
len(frase) # comprimento, quantidade de caracteres
frase.count('o',0,13) # contar quantas vezes aparece a letra o, do 0 ao 12
frase.find('deo') # indica a posição inicial do 'deo'
frase.find('Android') # vai indicar -1, significa que o item buscado não foi encontrado
'Curso' in frase # retorna true ou false, existe 'Curso' em frase?

# Transformação
frase.replace('Python', 'Android') # substitui Python por Android
frase.upper() # deixa tudo maiúsculo
frase.lower() # deixa tudo minúsculo
frase.capitalize() # deixa a primeira letra maiúscula
frase.title() # deixa a primeira letra de cada palavra maiúscula

frase1 = '   Apenda Python  '
frase1.strip() # remove os espaços inúteis
frase1.rstrip() # remove os espaços inúteis da direita
frase1.lstrip() # remove os espaços inúteis da esquerda

# Divisão
frase2 = 'Curso em Vídeo Python'
frase2.split() # divide a frase em pedaços, CURSO/EM/VIDEO/PYTHON

# Junção
'-'.join(frase2)