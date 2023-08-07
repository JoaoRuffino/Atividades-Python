frase = str(input('Insira uma frase: ')).strip().upper()

print("A frase '{}' possui {} A's".format(frase, frase.count('A')))
print('O primeiro "A" aparece na posição {}'.format(frase.find('A') + 1) )
print('O último "A" aparece na posição {}'.format(frase.rfind('A') + 1))