# Desafio 35 leia três comprimentos de reta e diga ao usuário se elas podem ou não formar um triangulo
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

'''if r1 < r1 + r2 and r2 < r1 + r3 and r3 < r1 + r2:
  print('Os segmentos de reta podem formar um triângulo')
else:
  print('Os segmentos de reta não podem formar um triângulo')'''

if r1 + r2 > r3:
  if r1 + r3 > r2:
    if r2 + r3 > r1:
      print('Os segmentos de reta podem formar um triângulo')
else:
  print('Os segmentos de reta não podem formar um triângulo')