print('TABUADA DE 1x A 10x')
r = 0
c = int(input('Qual tabuada deseja ver?'))
for n in range(1, 10+1, 1):
    r = c * n
    print('{} X {} = {}'.format(c, n, r))

