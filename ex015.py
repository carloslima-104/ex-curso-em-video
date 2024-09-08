print('Calculos de totais de aluguel de carro. Dia/km')
km = float(input('Digite a quantidade de km percorrido: '))*0.15
dias = int(input('Quantos dias permaneceu com o carro?'))*60
print('Com base nos dias e na distancia percorrida, o valor do aluguel do carro ficou em R${}'.format(km+dias))