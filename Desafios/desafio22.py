name = input('Insira seu nome: ').strip()
print('Seu nome com todas as letras em maiúsculo ficará: {}'.format(name.upper()))
print('Seu nome com todas as letras em minúsculo ficará: {}'.format(name.lower()))

name1 = name.replace(' ', '')
print('Seu nome possui {} letras'.format(len(name1)))

name2 = name.split()
print('Seu primeiro nome é {} e ele possui {} letras'.format(name2[0],len(name2[0])))