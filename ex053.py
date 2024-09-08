frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
'''inverso = junto[::-1]'''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('Você digitou {} e ao contrario fica {}'.format(frase, inverso))
if junto == inverso:
    print('Esta é uma frase políndromo')
else:
    print('Está NÃO é uma frase políndromo!')


