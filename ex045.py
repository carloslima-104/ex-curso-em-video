from random import randint
from time import sleep
print('-=-'*40)
print('~~~~~~~~JOKENPO~~~~~~~~')
jogador = int(input('Suas opções:\n[ 0 ]Pedra\n[ 1 ]Papel\n[ 2 ] Tesoura\n~~~~~~~~~~~~~~~~~~~~~~~~\nEscolha:'))
itens = ('PEDRA', 'PAPEL', 'TESOURA')
comp = randint(0,2)
print('-=-'*40)
print('JO')
sleep(1)
print('KEEN')
sleep(1)
print('PO!!!')
sleep(1)
print('jogador {} X {} computador'.format(itens[jogador], itens[comp]))
if comp == 0:
    if jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('JOGADOR PERDEU')
    elif jogador == 0:
        print('EMPATE')
if comp == 1:
    if jogador == 0:
        print('JOGADOR PERDEU')
    elif jogador == 2:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
if comp == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('JOGADOR PERDEU')
    elif jogador == 2:
        print('EMPATE')
print('-=-'*40)

