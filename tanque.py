c = int(input())
# consumo em km rodados por litro de combustivel
d = int(input())
# distância do aeroporto em km 
t = int(input())
# numero de litros de combustivel no tanque antes do abastecimento 

litros_precisos = d / c
abastecer = litros_precisos - t

if abastecer <= 0:
    print('0.0')
else:
    print(f'{abastecer:.1f}')