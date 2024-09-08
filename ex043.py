print('Calculando o IMC (índice massa corporal)')
alt = float(input('Qual é a sua altura?'))
peso = float(input('Qual é o seu peso?'))
imc = (peso / (alt**2))
#print('{:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('sobre peso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')