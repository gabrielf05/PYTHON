'''
Desafio 105 - Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
'''
def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    Notas = {}
    Notas['total'] = len(n)
    Notas['maior'] = max(n)
    Notas['menor'] = min(n)
    Notas['média'] = sum(n)/len(n)
    if sit:
        if Notas['média'] >= 7:
            Notas['situação'] = 'BOA'
        elif 5 <= Notas['média'] < 7:
            Notas['situação'] = 'RAZOÁVEL'
        else: 
            Notas['situação'] = 'RUIM'
    return Notas

resp = notas(5.5, 2.5, 5, 6.5, sit=True)
print(resp)
help(notas)