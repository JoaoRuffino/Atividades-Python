print('{:=^40}'.format(' LOJAS CEM '))
preço = float(input('Preço das Compras: R$'))
print('''Formas de pagamento:
 [ 1 ] à vista dinheiro/cheque
 [ 2 ] à vista no cartão
 [ 3 ] 2x no cartão
 [ 4 ] 3x ou mais no cartão''')
forma = int(input('Qual será a forma de pagamento? '))

if forma == 1:
    total = preço * 90/100
elif forma == 2:
    total = preço * 95/100
elif forma == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${}'.format(parcela))

elif forma == 4:
    total = preço * 120/100
    print('O total a ser pago com Juros será de R${:.2f}'.format(preço * 120/100))
    parcela = int(input('Em quantas vezes deseja parcelar? '))
    if parcela >= 3:
        print('O valor parcelado ficará: {}x de R${:.2f}'.format(parcela, (preço * 120/100)/parcela))
    else:
        print('Essa não é uma opção válida!!')

else:
    print('Opção não válida')
    total = preço
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))