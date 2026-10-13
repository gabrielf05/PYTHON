def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg))
        if entrada.isalpha():
            print(f'ERRO: \"{entrada}\" é um preço inválido')
        else:
            válido = True
            return float(entrada)