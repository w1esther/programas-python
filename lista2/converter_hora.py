hora = int(input())
minuto = int(input())

def converter(hora, minuto):

    if hora == 0:
        período = 'A.M'
        hora_12 = 12
    elif hora == 12:
        período = 'P.M'
        hora_12 = 12
    elif hora > 12:
        período = 'P.M'
        hora_12 = hora - 12
    else:
        período = 'A.M'
        hora_12 = hora
    
    return hora_12, minuto, período


h, m, p = converter(hora, minuto)

print(f'{h}:{m} {p}')