i = int(input('Qual número deve iniciar a sua razão?'))
p = int(input('Qual o passo deve ser respeitado na razão?'))
pa = 1
termos = 11
print('O inicío da sua razão é {} e o salto de {} em {}'.format(i, p, p))
while pa <= 10:
    print('{} '.format(i), end=' ')
    pa += 1
    i += p
