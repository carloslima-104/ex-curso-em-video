f = int(input('Digite um número para saber o seu fatorial:'))
multi = 1
for c in range(2, f + 1):
    print('{} '.format(c), end='')
    if c < f:
        print('x ', end='')
    multi = multi * c
print('\nO fatorial de {} é {}'.format(f, multi))
