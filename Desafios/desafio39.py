from datetime import date
genr = str(input('Você é do sexo masculino ou feminino? ')).strip().lower()
nasc = int(input('Insira seu ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, ano))
if idade < 18 and genr == 'masculino':
    print('Ainda faltam {} ano(s) para seu alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(nasc + 18))

elif idade > 18 and genr == 'masculino':
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}.'. format(nasc + 18))

elif idade == 18 and genr == 'masculino':
    print('Você deve se alistar IMEDIATAMENTE')

else:
    print('Você não precisa obrigatoriamente se alistar')