lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def media(lista):
    elementos_lista = len(lista)
    soma_elementos = sum(lista)
    media = soma_elementos/elementos_lista
    return media

media_numeros = media(lista)

print(media_numeros)