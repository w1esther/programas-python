lista_cosoantes = []

for n in range(1, 11):
    letra = input(f'Digite a {n}ª letra: ')

    if letra != 'A' and letra != 'a' and letra != 'E' and letra != 'e' and letra != 'I' and letra != 'i' and letra != 'o' and letra != 'O' and letra != 'u' and letra != 'U':
        lista_cosoantes.append(letra)

quantidade_consoantes = len(lista_cosoantes)

for i in lista_cosoantes:
    print(i, end=' ')
print(f'\na quantidade de consoantes digitadas foi de {quantidade_consoantes} consoantes ')