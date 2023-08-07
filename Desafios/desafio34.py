sal = float(input('Insira o salário do funcionário: R$'))
if sal > 1250.00:
    aument = sal * (10/100)
    print('O novo salário será de R${:.2f}'.format(sal + aument))

else:
    aument = sal * (15/100)
    print('O novo salário será de R${:.2f}'.format(sal + aument))

print('----FIM----')