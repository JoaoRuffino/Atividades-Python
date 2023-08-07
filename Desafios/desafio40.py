nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.2f} e {:.2f} a média do aluno será de {:.2f}'.format(nota1, nota2, media))
if media < 5.0:
    print('Você foi REPROVADO.')
elif 7 > media >= 5.0 :
    print('Você está de RECUPERAÇÃO.')
else:
    print('Você foi APROVADO.')