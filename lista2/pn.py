num = float(input())

def posi_neg(n):
    if n > 0:
        return 'P'
    else:
        return 'N'
    
resultado = posi_neg(num)

print(resultado)