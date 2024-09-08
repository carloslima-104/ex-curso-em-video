print('Calculando preço final do produto')
pn = float(input('Qual o preço normal do produto? R$'))
print(''''1. à vista (dinheiro ou cheque) 
2. à vista (cartão) 
3. 2x no cartão (S/ juros) 
4. 3x ou mais no cartão (20% de juros)')''')
fp = int(input('qual a forma de pagamento?'))
if fp == 1:
    pn = pn / 100 * 80
    print('Você recebeu 20% de desconto em seu produto. preço final do produto R${:.2f}'.format(pn))
elif fp == 2:
    pn = pn / 100 * 95
    print('Você recebeu 5% de desconto. Preço final do produto R${:.2f}'.format(pn))
elif fp == 4:
    pn = pn / 100 * 120
    print('O seu produto receberá o valor de R${:.2f} em 3x ou mais no cartão'.format(pn))
elif fp == 3:
    print('O seu produto permanecerá em R${:.2f} em 2x no cartão'.format(pn))
