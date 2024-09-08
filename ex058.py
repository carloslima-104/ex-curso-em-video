from random import randint
from time import sleep
print('-*-' *20)
print('Lets bora. Iniciando o jogo...')
print('-*-' *20)
cont = 0
jog = ''
comp = 0
while jog != comp:
    jog = int(input('Em qual numero acha que estou pensando de 0 a 10? '))
    comp = (randint(0, 10))
    cont += 1
    print('Analisando...')
    sleep(0.5)
    if comp == jog:
        print('PARABÉNS, você acertou. Eu estava pensando no numero {}!!!'.format(comp))
        print('Você precisou de {} tentativas para acertar'.format(cont))
    else:
        print('Infelizmente você errou, pensei no numero {}!'.format(comp))

    print('-*-' * 20)
