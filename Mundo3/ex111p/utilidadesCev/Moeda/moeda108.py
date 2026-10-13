def metade(n=0):
    resp = n / 2
    return resp


def dobro(n=0):
    resp = n * 2
    return resp


def aumentar(n=0, x=0):
    resp = n + (n / 100) * x
    return resp


def diminuir(n=0, x=0):
    resp = n - (n / 100) * x
    return resp 


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')