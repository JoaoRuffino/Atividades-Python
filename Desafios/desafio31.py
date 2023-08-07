dist = float(input('Qual a distância da viagem em Km? '))
if dist <= 200:
    passag = (dist * 0.5)
    print('Por se tratar de uma viagem de até 200 Km, o preço da passagem será de R${:.2f}'.format(passag))
else:
    passag = (dist * 0.45)
    print('Por se tratar de uma viagem de mais de 200 Km, o preço da passagem será de R${:.2f}'.format(passag))

print('Boa viagem!!')