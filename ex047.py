'''i = int(input('Número onde deve iniciar a contagem: '))
f = int(input('Número onde a contagem deve parar: '))
n = i % 2
print('Os números pares entre {} e {} são: '.format(i,f))
if n == 0:
    for n in range(i, f+1, 2):
        print('{},'.format(n), end=(''))
else:
    for n in range(i+1, f+1, 2):
        print('{},'.format(n), end=(''))'''
for cont in range(2, 51, 2):
    print(' {}'.format(cont), end=(''))

