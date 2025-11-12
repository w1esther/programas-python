preco_total = 0

for n in range(1, 11):
    valor = float(input(f'digite o valor pago no {n}º produto: '))
    preco_total += valor

print(f'o valor total da compra foi de {preco_total} reais')