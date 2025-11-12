import statistics

lista_nomes = []
lista_idades = []

for n in range(1, 6):
    nome = input(f'digite o nome da {n}ª pessoa: ')
    lista_nomes.append(nome)
    idade = int(input(f'digite a idade da {n}ª pessoa: '))
    lista_idades.append(idade)

maior_idade = max(lista_idades)
indice1 = lista_idades.index(maior_idade)
nome_maior = lista_nomes[indice1]

menor_idade = min(lista_idades)
indice2 = lista_idades.index(menor_idade)
nome_menor= lista_nomes[indice2]

media = statistics.mean(lista_idades)

print(f'o nome da pessoa mais nova é {nome_menor} e sua odade é de {menor_idade} anos. O nome da pessoa mais velha é {nome_maior} e sua idade é de {maior_idade} anos. A média de todas as idades é {media}')
