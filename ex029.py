km = int(input('Seu carro está a quantos km/h?'))
multa = (km - 80)*7
if km <= 80:
    print('Você está dentro do limite permitido')
else:
    print('Você foi multado! isso custará R$7 por km/h acima do permitido, totalizando R${} em multa'.format(multa))
