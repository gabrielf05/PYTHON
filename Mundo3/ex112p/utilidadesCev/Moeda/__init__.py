def metade(n=0, formatar=False):
    resp = n / 2
    if formatar == False:
        return resp
    else:
        return moeda(resp)


def dobro(n=0, formatar=False):
    resp = n * 2
    if formatar == False:
        return resp
    else:
        return moeda(resp)


def aumentar(n=0, x=0, formatar=False):
    resp = n + (n / 100) * x
    if formatar == False:
        return resp
    else:
        return moeda(resp)


def diminuir(n=0, x=0, formatar=False):
    resp = n - (n / 100) * x
    if formatar == False:
        return resp
    else:
        return moeda(resp)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(preço=0, aumento=0, redução=0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço análisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'Aumento de {aumento}%: \t{aumentar(preço, aumento, True)}')
    print(f'Redução de {redução}%: \t{diminuir(preço, redução, True)}')
    print('-'*30)
    
