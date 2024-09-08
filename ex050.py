soma = 0
cont = 0
for c in range(1, 7):
    numero = int(input('Digite o {}° numero:'.format(c)))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print('Você digitou {} números pares e a soma deles foram {}'.format(cont,soma))
