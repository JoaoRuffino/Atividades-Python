num = int(input('Insira um número inteiro: '))
conv = int(input('Deseja converter para binário(1), octal(2), ou hexadecimal(3)? '))

if conv == 1:
    binario = bin(num)
    print('O número {} convertido para a base 2 fica {}{}{}'.format(num, '\033[32m', binario[2:], '\033[m'))
elif conv == 2:
    octal = oct(num)
    print('O número {} convertido para a base 8 fica {}{}{}'.format(num, '\033[32m', octal[2:], '\033[m'))
elif conv == 3:
    hexa = hex(num)
    print('O número {} convertido para a base 16 fica {}{}{}'.format(num, '\033[32m', hexa[2:], '\033[m'))
else:
    print('A conversão escolhida é {}inválida{}'.format('\033[0;31m', '\033[m'))