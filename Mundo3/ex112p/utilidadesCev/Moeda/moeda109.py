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