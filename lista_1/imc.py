imc = float(input('digite seu índice de massa corporal (IMC): '))

if imc > 25.0:
    print('Você está acima do peso!')
elif 18 <= imc <= 24.9:
    print('Você está em seu peso normal!')
else:
    print('Você está abaixo do peso!')
