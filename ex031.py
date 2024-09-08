dis = int(input('Qual a distância da viagem em km? '))
vc = (dis * 0.50)
vl = (dis * 0.45)
if dis <= 200:
    print('Sua viagem é curta e vai custar o valor de R${:.2f}'.format(vc))
else:
    print('Sua viagem é longa e vai te custar o valor de R${:.2f}'.format(vl))