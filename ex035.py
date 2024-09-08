print('-=-' * 20)
print('Descobrindo se conseguimos fazer um triângulo com 3 retas ')
print('-=-' * 20)
r1 = float(input('Qual a primeira medida em cm? '))
r2 = float(input('E a segunda?'))
r3 = float(input('E a terceira?'))
'''if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
     print('Os segmentos acima PODEM FORMAR um triângulo')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')'''
maior = r1
if r2>r1 and r2>r3:
    maior = r2
if r3>r1 and r3>r2:
    maior = r3
if ((r1+r2+r3)-maior)>maior:
    print('OPA! Conseguiremos fazer um triangulo com essas medidas')
else:
    print('NÃO podemos fazer um triângulo com essas medidas')