import emoji
from time import sleep
print('CONTAGEM REGRESSIVA PARA O ESTOURO DE FOGOS!')
cont = str(input('Aperte enter para começar'))
for i in range(10, 0-1, -1):
    print(i)
    sleep(1)
print(emoji.emojize(':party_popper:'*5))
print('POW, POW ,BOOM!')