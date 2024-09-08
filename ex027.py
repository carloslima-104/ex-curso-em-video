nome = str(input('Digite seu nome completo:')).strip().lower()
repart = nome.split()
print('Seu primeiro nome é {}'.format(repart[0]))
print('Seu último nome é {}'.format(repart[-1]))

#print('Seu primeiro nome é {}'.format(nome.split()[0]))