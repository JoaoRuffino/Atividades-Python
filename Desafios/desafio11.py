larg = float(input('Insira a largura de sua parede em metros: '))
alt = float(input('Insira a altura de sua parede em metros: '))
area = larg * alt
print('Sua área é de {} metros quadrados'.format(area))
tint = area / 2
print('Será(ão) necessário(s) {} litro(s) de tinta para a pintura dessa parede'.format(tint))