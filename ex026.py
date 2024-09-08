nome = str(input('Digite a sua frase: ')).strip().lower()
print("na sua frase tem {} letras 'a'".format(nome.count('a')))
print("a primeira letra 'a' está na posição {} e a ultima na posição {} ".format(nome.find('a')+1,nome.rfind('a')+1))