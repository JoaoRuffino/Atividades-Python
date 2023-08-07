from random import randint
from time import sleep

num = randint(0, 5)
print('-=-'*20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print('-=-'*20)
tent = int(input('Em que número eu pensei? '))
print("Processando...")
sleep(3)
print('-=-'*20)
if tent == num:
    print('Parabéns você acertou! O número escolhido foi {}'.format(num))
else:
    print('Infelizmente você errou. O número escolhido foi {}'.format(num))
    
print('-=-'*20)
