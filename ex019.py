from random import choice
alu1 = str(input('Nome do aluno: '))
alu2 = str(input('nome do aluno: '))
alu3 = str(input('nome do aluno: '))
alu4 = str(input('nome do aluno: '))
lista = [alu1, alu2, alu3, alu4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
