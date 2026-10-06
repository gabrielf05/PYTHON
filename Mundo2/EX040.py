# Desafio 40

n1 = float(input('Digite a primeiro nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) / 2

if média < 5.0:
    print('A média do aluno é {}, ele está REPROVADO.'.format(média))
elif média >= 5 and média <= 6.9:
    print('A média do aluno é {}, ele está de RECUPERAÇÃO.'.format(média))
elif média >= 7.0:
    print('A média do aluno é {}, ele está APROVADO.'.format(média))