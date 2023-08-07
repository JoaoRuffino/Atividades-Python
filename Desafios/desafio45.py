from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print('''Suas Opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual a sua jogada? '))

computador = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)

print('-=' * 15)
if 0  <= jogador <= 2:
    
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    

else:
    print('Jogada Inválida :( ')
print('-=' * 15)

if computador == 0:
    if jogador == 0:
        result = 'EMPATE'
    elif jogador == 1:
        result = 'VOCÊ VENCEU!'
    elif jogador == 2:
        result = 'EU VENCI HEHE'
    else:
        result = 'Jogada Inválida'

elif computador == 1:
    if jogador == 0:
        result = 'EU VENCI HEHE'
    elif jogador == 1:
        result = 'EMPATE'
    elif jogador == 2:
        result = 'VOCÊ VENCEU!'
    else:
        result = 'Jogada Inválida'

else:
    if jogador == 0:
        result = 'VOCÊ VENCEU!'
    elif jogador == 1:
        result = 'EU VENCI HEHE'
    elif jogador == 2:
        result = 'EMPATE'
    else:
        result = 'Jogada Inválida'

print('Resultado do Jogo: {}'.format(result))