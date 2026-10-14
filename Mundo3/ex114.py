'''
Desafio 114 - Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
'''

import requests

url = "https://pudim.com.br/"

try:
  # timeout=5 evita que o script trave se o site estiver muito lento
  resposta = requests.get(url, timeout=5)

  # Código 200 significa OK (site disponível)
  if resposta.status_code == 200:
    print(f"O site {url} está disponível! (Status: {resposta.status_code})")
  else:
    print(
        f"O site respondeu, mas com um código diferente: {resposta.status_code}"
    )

except requests.exceptions.RequestException as e:
  print(f"O site está inacessível ou ocorreu um erro: {e}")