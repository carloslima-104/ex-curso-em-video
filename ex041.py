from datetime import date
ano = int(input('Para saber em qual categoria o atleta se encaixa, digite o ano que o atleta nasceu? '))
idade = date.today().year - ano
print('O atleta tem {} anos'.format(idade))
if idade >= 25:
        print('MASTER')
elif idade >=10 and idade <= 14:
    print('INFANTIL')
elif idade >14 and idade <20:
    print('JUNIOR')
elif idade >19 and idade <=24:
    print('SENIOR')
else:
    print('MIRIM')