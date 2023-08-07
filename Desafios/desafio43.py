peso = float(input('Insira seu peso em kg: '))
altura = float(input('Insira sua altura em metros: '))
imc = peso / pow(altura, 2)
print('Seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc <= 25:
    print('Você está no peso ideal.')
elif imc <= 30:
    print('Você está no sobrepeso.')
elif imc <= 40:
    print('Você está na obesidade.')
else:
    print('Você está na obesidade mórbida.')