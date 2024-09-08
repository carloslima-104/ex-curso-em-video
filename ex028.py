import emoji
from random import randint
from time import sleep
comp = (randint(0,5))
print('-*-' *20)
print('Lets bora. Iniciando o jogo...')
print('-*-' *20)
jog = int(input('Em qual numero acha que estou pensando de 0 a 5? '))
print('Analisando...')
sleep(2)
if comp == jog:
    print('PARABÉNS, você acertou. Eu estava pensando no numero {}!!!'.format(comp))
else:
    print('Infelizmente você errou, pensei no numero {}!'.format(comp))
print('-*-' * 20)