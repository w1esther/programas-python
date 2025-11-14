lista_inversa = []

for n in range(1, 11):
    numero = float(input(f'digite o {n}º número: '))
    lista_inversa.append(numero)

for i in reversed(lista_inversa):
    print(i, end=' ')