user = "s"
maior = menor = soma = cont = 0

while user in "Ss":
    n = int(input("Digite um número inteiro: \n"))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if maior < n:
            maior = n
        if n < menor:
            menor = n
    user = str(input("Deseja continuar? [S/N] \n").lower().strip())


print("A média entre os {} números digitados é de {}, o maior digitado é o {} e o menor {}".format(cont, soma/cont, maior, menor))


