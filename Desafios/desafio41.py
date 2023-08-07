from datetime import date
nasc = int(input('Insira o ano de nascimento do atleta: '))
idade = date.today().year - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Categoria: MIRIM')

elif idade <= 14:
    print('Categoria: INFANTIL')

elif idade <= 19:
    print('Categoria: JÚNIOR')

elif idade <=25:
    print('Categoria: SÊNIOR')

else:
    print('Categoria: MASTER')