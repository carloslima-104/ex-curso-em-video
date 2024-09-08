i = int(input('Digite o número que acha que é um número primo?'))
div = 0
for c in range(1, i+1, 1):
    if i % c == 0:
        print('\033[34m', end='')
        div += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(i, div))
if div == 2:
    print('Este é um número primo!')
else:
    print('este não é um número primo')
