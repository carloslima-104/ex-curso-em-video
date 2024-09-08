f = int(input('Digite um número para saber o seu fatorial:'))
c = f
multi = 1
while c > 0:
    print(' {} '.format(c), end='')
    print('x' if c > 1 else '=', end='')
    multi *= c
    c -= 1
print('\nO fatorial de {} é {}'.format(f, multi))
