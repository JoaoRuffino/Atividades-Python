valor = float(input('Insira o valor da casa que deseja adquirir: R$'))
salario = float(input('Insira o seu salário: R$'))
anos = int(input('Insira em quantos anos você irá pagar: '))
meses = anos * 12
prest = valor / meses
if prest > (salario * 30/100):
    print('Seu empréstimo bancário foi {}negado!{}. O valo da prestação mensal seria de R${:.2f} por mês '.format('\033[0;31m', '\033[m', prest))
else:
    print('Seu empréstimo foi {}aprovado!{} O valo da prestação mensal será de R${:.2f} por mês'.format('\033[0;32m', '\033[m', prest))
    