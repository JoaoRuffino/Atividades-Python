from math import sqrt, pow
#from math import hypot
co = float(input('Digite o valor do cateto oposto em metros: '))
ca = float(input('Digite o valor do cateto adjacente em metros: '))
hipotenusa = sqrt(pow(co, 2) + pow(ca, 2))
#hipotenusa = hypot(co, ca)

print('O valor da hipotenusa desse triângulo retângulo é {:.2f} metros'.format(hipotenusa))