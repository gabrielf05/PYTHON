# Desafio 43


altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Você tem um IMC de {:.2f}, você está abaixo do peso'.format(imc))
elif 18.5 <= imc < 25:
    print('Você tem um IMC de {:.2f}, você está no peso ideal'.format(imc))
elif 25 <= imc < 30:
    print('Você tem um IMC de {:.2f}, você está com sobrepeso'.format(imc))
elif 30 <= imc < 40:
    print('Você tem um IMC de {:.2f}, você está em um caso de obesidade'.format(imc))
else:
    print('Você tem um IMC de {:.2f}, você está em um caso de obesidade mórbida'. format(imc))