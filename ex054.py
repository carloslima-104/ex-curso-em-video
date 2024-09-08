from datetime import date
menor = 0
maior = 0
for a in range(1, 8):
    ano = int(input('Qual ano de nascimento?'))
    if date.today().year - ano < 21:
        menor += 1
    else:
        maior += 1
print('Desses citados, {} são maiores {} são menores de idade'.format(maior, menor))
