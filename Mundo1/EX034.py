# Desafio 34 Pergunte o slario do funcionario e calcule seu aumento(maiores que 1250 aumento de 10%, menores aumento de 15%)
s = float(input('Digite o seu salário: '))
if s > 1250:
  print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(s,s*1.1))
else:
  print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(s,s*1.15))