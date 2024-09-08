i = int(input('Qual número deve iniciar a sua razão?\n'))
p = int(input('Qual o passo deve ser respeitado na razão?\n'))
mais = 10
print('O inicío da sua razão é {} e o salto de {} em {}'.format(i, p, p))
cont = mais
while True:
    pa = 0
    curr_i = i
    while pa <= mais:
        print('{} '.format(curr_i), end='')
        pa += 1
        curr_i += p
    ver_mais = int(input('\nVer mais alguns termos? [1] - SIM, [2] - NÃO\n' ))
    if ver_mais == 1:
        termos = int(input('Quantos?\n'))
        i = curr_i
        mais = termos
        cont += termos
    elif ver_mais == 2:
        print('finalizado com {} termos mostrados'.format(cont))
        print('fim')
        break
    else:
        print('Opção invalída, por favor, escolha: [1] - SIM, [2] - NÃO.')
