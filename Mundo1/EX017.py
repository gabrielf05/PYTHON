import math

ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))
#hi = math.sqrt((ca**2)+(co**2))
hi = math.hypot(ca,co)
print('O valor do cateto adjacente é {}, do cateto oposto é {} e a hipotenusa é {}.'. format(ca, co, hi))