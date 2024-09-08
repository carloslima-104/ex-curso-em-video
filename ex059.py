soma = 0
maior = 0

while True:
    n1 = int(input('Primeiro número: \n'))
    n2 = int(input('Segundo número: \n'))

    if n1 == 0 or n2 == 0:
        break

    while True:
        print('[ 1 ] Somar')
        print('[ 2 ] Multiplicar')
        print('[ 3 ] Maior')
        print('[ 4 ] Novos números')
        print('[ 5 ] Sair do programa')
        print('--' * 20)

        esc = int(input('Qual a opção desejada? \n'))

        if esc == 1:
            soma = n1 + n2
            print('A soma de {} + {} equivale a {}'.format(n1, n2, soma))
        elif esc == 2:
            multi = n1 * n2
            print('{} X {} é igual a {}'.format(n1, n2, multi))
        elif esc == 3:
            if n1 > n2:
                maior = n1
            else:
                maior = n2
            print('O maior número entre {} e {} é {}'.format(n1, n2, maior))
        elif esc == 4:
            break  # Sai do loop interno e pede novos números
        elif esc == 5:
            print('Finalizando, volte sempre!')
            n1 = 0  # Define n1 como 0 para sair do loop externo
            break
        else:
            print('Opção inválida')

        print('--' * 20)

    if n1 == 0:
        break

print('Fim')

