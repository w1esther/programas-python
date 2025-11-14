lista_numeros = []

for n in range(1, 6):
    numero = float(input(f'digite o {n}º número: '))
    lista_numeros.append(numero)

for i in lista_numeros:
    print(i, end=' ')