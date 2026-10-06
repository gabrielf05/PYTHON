# Desafio 62 - Melhore o desafio 61, o programa vai ler mostrar os 10 primeiros termos e perguntar quando mais termos o usuário quer mostrar, termina quando ele disser 0

termo = int(input('Dgite o primeiro termo da sua PA: '))
razao = int(input('Diigte a razão da sua PA: '))
primeiro = termo
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} - > '.format(primeiro), end='')
        primeiro = primeiro + razao
        c = c + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('progressão finalizada com {} termos mostrados'.format(c - 1))



'''
  if c > 10:
    print('PAUSA')
    primeiro = int(input('Quantos termos você quer mostrar a mais? '))
    if primeiro == 0:
        print('FIM')
    else:
        print('{} - > '.format(primeiro), end='')
        primeiro = primeiro + razao
        c = c + 1'''