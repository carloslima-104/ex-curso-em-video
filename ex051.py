i = int(input('Qual número deve iniciar a sua razão?'))
r = int(input('Qual o passo deve ser respeitado na razão?'))
pa = i + (10 - 1) * r
print('O inicío da sua razão é {} e o salto de {} em {}'.format(i, r, r))
for c in range(i, pa, r):
    print('{}'.format(c), end=' ')

