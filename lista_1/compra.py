preco_total = float(input('digite o valor total da compra: '))

valor_pagamento = float(input('digite o valor dado para o pagamento: '))

troco = valor_pagamento - preco_total

if troco < 0:
    print('valor insuficiente para pagar a compra')
else:
    troco_real = troco
