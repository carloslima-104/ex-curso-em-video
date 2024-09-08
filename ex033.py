import math
n1 = int(input('Digite o primeiro numero:'))
n2 = int(input('O segundo:'))
n3 = int(input('O terceiro:'))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O maior numero é {} e o menor é {}'.format(maior,menor))

