# Desafio 29

v = float(input('Informe a velocidade que você passou no radar: '))
limite = 80
multa = (v-limite)*7
if v > limite:
  print('O limite de velocidade é {} Km/h, você ultrapassou por {} Km/h. Você vai pagar R$ {:.2f} de multa'.format(limite, v-limite, (multa)))
else:
  print('Você está dentro do limite de velocidade')