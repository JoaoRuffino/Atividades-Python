from math import trunc

real = float(input('Digite um número real: '))
inteiro = trunc(real)

print('A porção inteira do número {} é {}'.format(real, inteiro))