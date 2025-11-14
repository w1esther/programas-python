lista_notas = []

for n in range(1, 5):
    nota = float(input(f'digite a {n}ª nota: '))
    lista_notas.append(nota)

soma_notas = 0

for i in lista_notas:
    soma_notas += i

quantidade_elementos = len(lista_notas)

media_notas = soma_notas / quantidade_elementos

for l in lista_notas:
    print('nota:', l, end=' ')
print('\n','media das notas:', media_notas)