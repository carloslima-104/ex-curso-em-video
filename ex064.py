num = soma = cont = 0
while num != 999:
    num = int(input("digite um número inteiro:[999 para parar]\n"))
    if num != 999:
        cont += 1
        soma = soma + num
print('Você digitou números {} vezes e a soma deles é {}'.format(cont, soma))

