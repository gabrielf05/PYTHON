# Desafio 26
# faça um programa que leia uma frase pelo teclado e mostre
# Quantas vezes aparece a letra a
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

fr = str(input('Digite uma frase:')).upper().strip()
print("A letra 'a' aparece {} vezes na frase".format(fr.count('A')))
print("A primeira letra 'a' apareceu na posição {}".format(fr.find('A')+1))
print("A última letra 'a' apareceu na posição {}".format(fr.rfind('A')+1)) #rfind procura partindo do lado direito