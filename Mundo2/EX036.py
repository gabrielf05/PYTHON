# Desafio 36
s = float(input('Qual o seu salário? '))
c = float(input('Qual o valor da casa que você quer comprar? '))
t = int(input('Em quantos anos você quer pagar o financiamento? '))

prazo = t * 12
parcela = c / prazo
parcela_max = s * (30 / 100)

print('Para pagar uma casa de RS {:.2f} em {:.2f} anos a prestação será de {:.2f}'.format(c, t, parcela))
if parcela <= parcela_max:
    print('Parabéns, seu financiamento foi aprovado!')
else:
    print('Infelizmente, seu financiamento foi negado!')

