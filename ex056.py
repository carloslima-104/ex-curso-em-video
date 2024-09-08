somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0
for i in range(1, 5):
    print('------ {}° Pessoa------'.format(i))
    nome = str(input('Qual o nome da {}° pessoa: '.format(i))).upper().strip()
    idade = int(input('Qual a idade da {}° pessoa: '.format(i)))
    somaidade += idade
    mediaidade = somaidade / 4
    sexo = str(input('Sexo da {}° pessoa: [M/F] '.format(i))).upper().strip()

    if i == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'fF' and idade < 20:
        totmulher += 1

print('A media da idade do grupo é de {}'.format(mediaidade))
print('O nome do homem mais velho é {} e a sua idade é {}'.format(nomevelho, maioridadehomem))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher))
