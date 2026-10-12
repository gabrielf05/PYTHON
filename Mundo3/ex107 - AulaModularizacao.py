'''
MÓDULOS
Surgiu nos anos 60
Vantagens:
- Organização do código
- Facilidade na manutenção
- Ocultação do código detalhado
- Reutilizar em outros projetos
'''

import modulos.uteis.numeros.uteis as uteis

num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}')
print(f'O triplo de {num} é {uteis.triplo(num)}')

'''
PACOTES
Junção de módulos e separados por assunto (pasta que contém módulos)
Pacote uteis
    modulo numeros
    modulo datas
    modulo cores
    modulo strings
    
import uteis
from uteis import datas
'''
