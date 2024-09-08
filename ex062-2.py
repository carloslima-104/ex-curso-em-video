i = int(input('Qual número deve iniciar a sua razão? '))
p = int(input('Qual o passo deve ser respeitado na razão? '))
termos = 11

print('O início da sua razão é {} e o salto de {} em {}'.format(i, p, p))

while True:
    pa = 0
    current_i = i
    while pa < termos:
        print('{} '.format(current_i), end=' ')
        pa += 1
        current_i += p
    print()  # Adiciona uma nova linha após exibir os termos

    ver_mais = int(input('Ver mais alguns termos? [1] - SIM, [2] - NÃO: '))
    if ver_mais == 1:
        termos = int(input('Quantos? '))
        i = current_i  # Atualiza o valor inicial para o próximo ciclo
    elif ver_mais == 2:
        print('Fim')
        break
    else:
        print('Opção inválida, por favor, escolha [1] - SIM ou [2] - NÃO.')