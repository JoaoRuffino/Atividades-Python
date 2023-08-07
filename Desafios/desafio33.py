num1 = float(input('Escreva o primeiro número: '))
num2 = float(input('Escreva o segundo número: '))
num3 = float(input('Escreva o terceiro número: '))

if num1 > num2 > num3:
    print('O maior número é {} e o menor número é {}'.format(num1, num3))

if num1 > num3 > num2:
    print('O maior número é {} e o menor número é {}'.format(num1, num2))

if num3 > num2 > num1:
    print('O maior número é {} e o menor número é {}'.format(num3, num1))

if num3 > num1 > num2:
    print('O maior número é {} e o menor número é {}'.format(num3, num2))

if num2 > num1 > num3:
    print('O maior número é {} e o menor número é {}'.format(num2, num3))

if num2 > num3 > num1:
    print('O maior número é {} e o menor número é {}'.format(num2, num1))

else:
    print('Você digitou número iguais. Não Pode!!!')
