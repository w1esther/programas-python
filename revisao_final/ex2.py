texto = input('digite um texto e direi quantas vogais tem: ')
lista_texto = list(texto)
vogais = []

for n in lista_texto:
    if n == 'a' or n == 'A' or n == 'o' or n == 'O' or n == 'I' or n == 'i' or n == 'e' or n == 'E' or n == 'u' or n == 'U':
        vogais.append(n)

num_vogais = len(vogais)

print(f'esse texto tem {num_vogais} vogais')