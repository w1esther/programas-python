distancia = float(input('forneça a distância que seu veículo irá percorrer: '))

km_por_litro = float(input('forneça quantos quilômetros o seu vículo roda por litro: '))

abastecer = distancia / km_por_litro

print(f'é preciso abastecer o seu veículo com {abastecer} litros')