lista_idades = []
lista_nomes = []

for n in range(1, 6):
    idade = float(input(f'digite a idade da {n}ª pessoa: '))
    lista_idades.append(idade)

    nome = input(f'digite o nome da {n}ª pessoa')
    lista_nomes.append(nome)

print('Idades:')

for i in reversed(lista_idades):
    print(i, end='')

print('\nNomes:')

for k in reversed(lista_nomes):
    print(k, end=' ')