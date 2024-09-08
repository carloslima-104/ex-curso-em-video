valor = float(input('Qual o valor da casa que tem interesse? R$'))
salario = float(input('Qual o seu salário mensal? R$'))
anos = int(input('Em quantos anos pretende pagar o imóvel? '))*12

parc = valor / anos
toler = salario * 30 / 100
if parc <= toler:
    print('Sua oferta de empréstimo foi \033[1:32:40mAPROVADA\033[m')
    print('A sua parcela ficaria no valor de R${:.2f}.'.format(parc))
else:
    print('Não será possível a aprovação do seu empréstimo!')
    print('A sua parcela seria superior a tolerância')