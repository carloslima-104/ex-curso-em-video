n1 = float(input('Qual a sua primeira nota?'))
n2 = float(input('Qual a sua segunda nota?'))
media = (n1 + n2) / 2
if media < 5:
    print('Você está reprovado!')
elif media >= 5 and media < 7:
    print('Você está de recuperação!')
else:
    print('Você foi aprovado!')
