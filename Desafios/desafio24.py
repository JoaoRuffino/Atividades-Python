cida = str(input('Insira o nome da sua cidade: '))

num = cida.strip().upper().count('SANTO', 0)
if num == 1:
    print('Sua cidade começa com "Santo"')
else:
    print('Sua cidade não começa com "SANTO"')