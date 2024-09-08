n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número'))
maior = n1
if n2 > n1:
    maior = n2
    print('O segundo valor é maior')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais')
else:
    print('O primeiro valor é maior')
