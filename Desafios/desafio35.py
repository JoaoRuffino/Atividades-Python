
r1 = float(input('Insira o comprimento em metros da primeira reta: '))
r2 = float(input('Insira o comprimento em metros da segunda reta: '))
r3 = float(input('Insira o comprimento em metros da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('É possível formar um triângulo.')


else:
    print('Não é possível formar um triângulo')

print("---FIM---")