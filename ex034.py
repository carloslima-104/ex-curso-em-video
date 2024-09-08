sal = float(input('Qual o seu salário? R$'))
'''sa = sal * 0.10 if sal >= 1250 else sal * 0.15
print('Após o aumento salarial, você receberá R${} mensais'.format(sa+sal))'''
if sal <= 1250:
    novo = sal + (sal * 15/100)
else:
    novo = sal + (sal * 10/100)
print('O seu salário antigo de R${} recebeu uma alteração e foi para R${}'.format(sal,novo))
