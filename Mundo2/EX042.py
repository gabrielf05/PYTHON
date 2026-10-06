# Desafio 42

l1 = float(input('Primeiro segmento de reta: '))
l2 = float(input('Segundo segmento de reta: '))
l3 = float(input('Terceiro segmento de reta: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 == l2 == l3:
        print('Os segmentos de reta acima podem formar um triângulo EQUILÁTERO.')
    elif l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
       print('Os segmentos de reta acima podem formar um triângulo ISÓSCELES')
    elif l1 != l2 != l3: 
       print('Os segmentos de reta acima podem formar um triângulo ESCALENO')
else:
  print('Os segmentos de reta acima não podem formar um triângulo')
