dias = int(input('Quanto dias alugados? '))
km = float(input("Quantos Km rodados? "))

valor = (60 * dias) + (0.15 * km)

print('O valor a ser pago é de R${}'.format(valor))