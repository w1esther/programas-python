num = int(input('digite um número e direi se ele é primo ou não: '))

divisores = []

def eh_primo(n):
    for i in range(1, n + 1):
        divisao = n/i
        if n % i == 0:
            divisores.append(divisao)
    num_divisores = len(divisores)
    # print(num_divisores)
    if num_divisores == 2:
        return True
    else:
        return False
    
num_primo = eh_primo(num)

print(num_primo)