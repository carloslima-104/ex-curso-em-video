import math
co = float(input('Digite o numero do cateto oposto:'))
ca = float(input('Digite o numero do catato adjacente: '))
hi = math.hypot(co,ca)
'''hi = (co** 2 + ca ** 2) ** (1/2)
print('O valor da hipotenusa é {:.2f}'.format(hi))'''
print('A hipotenusa vai medir {:.2f}'.format(hi))