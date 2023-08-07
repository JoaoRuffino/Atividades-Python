veloc = float(input('Insira a velocidade do carro em Km/h: '))
if veloc <= 80:
    print('Nenhuma multa foi aplicada.')
else:
    mult = (veloc - 80) * 7
    print('Você foi multado em R${.:2f}'.format(mult))
