from datetime import date
print('-*'*40)
print('\033[34mConferindo idade para alistamento militar\033[m')
print('-*'*40)
nasc = int(input('Qual o ano de seu nascimento?'))
ano = date.today().year - 18
at = date.today().year
idade = at - nasc
print('Você tem {} anos em {}'.format(idade,at))
if nasc > ano:
    print('Você ainda irá se alistar')
elif nasc < ano:
    print('Já passou do tempo de se alistar ao serviço militar')
else:
    print('VOCÊ ESTÁ NO ANO PERFEITO PARA O ALISTAMENTO MILITAR')
