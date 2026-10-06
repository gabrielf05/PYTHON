c = float(input('Informe  o comprimento da parede:'))
l = float(input('Informe a largura da parede:'))
a = c*l
# 1 litro de tinta pinta 2m²
t = a/2

print('A área da sua parede é {}m², para pintá-la por inteiro será necessário {} litros de tinta'.format(a,t))