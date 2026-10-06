# Desafio 31 pergunte a distancia de uma viagem em KM e calcule o preço da passagem cobrando 0,50/km até 200km e 0,45/km para vinagens mais longas
d = float(input('Qual a distância da sua viagem? '))
if d <= 200:
  p1 = d * 0.5
  print('O preço da sua passagem é R$ {:.2f}'.format(p1))
else:
  p2 = d * 0.45
  print('O preço da sua passagem é R$ {:.2f}'.format(p2))
