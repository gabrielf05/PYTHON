d = int(input('Por quantos você alugou o carro? '))
km = float(input('Quando quilometros você percorreu? '))
valor = (d * 60) + (km * 0.15)
print('Você deve pagar o valor total de R${:.2f}'.format(valor))