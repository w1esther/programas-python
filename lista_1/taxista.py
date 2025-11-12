numero_viagens = int(input('digite o número de viagens realizadas no dia: '))

faturamento = 0

for n in range(1, (numero_viagens + 1)):
    valor_pago = float(input(f'digite o valor pago na {n}ª viagem: '))
    faturamento += valor_pago

print(f'o faturamento total no dia foi de {faturamento} reais!')