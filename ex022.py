nome = input('Digite seu nome:').strip()
print('analisando seu nome...')
print('Seu nome em letras maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}.'.format(nome.lower()))
#print('Seu nome tem {} letras é.'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))

