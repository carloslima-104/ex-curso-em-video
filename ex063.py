num_termos = int(input('Quantos termos da sequência de Fibonacci você deseja ver? '))

# Inicializa os primeiros termos da sequência
termo_atual = 0
proximo_termo = 1
contador = 0

# Verifica se o usuário deseja ver pelo menos 1 termo
if num_termos > 0:
    print('Os primeiros {} termos da sequência de Fibonacci são:'.format(num_termos))

# Gera e exibe os termos da sequência
while contador < num_termos:
    print(termo_atual, end=' ')

    # Calcula o próximo termo da sequência
    novo_termo = termo_atual + proximo_termo
    termo_atual = proximo_termo
    proximo_termo = novo_termo

    contador += 1

print()  # Nova linha após a sequênciainha após a sequência