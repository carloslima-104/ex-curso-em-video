i = int(input('Digite o número:'))
div = 0
for c in range(1, i+1, 1):
    if i % c == 0:
        div += 1
if div == 2:
    print('Este é um número primo!')
else:
    print('Este NÃO é um número primo')
