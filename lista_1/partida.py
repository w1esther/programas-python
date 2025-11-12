time1 = input('digite o nome do primeiro time: ')
time2 = input('digite o nome do segundo time: ')

gols_time1 = int(input(f'digite a quantidade de gols marcados pelo {time1}: '))
gols_time2 = int(input(f'digite a quantidade de gols marcados pelo {time2}: '))

if gols_time1 > gols_time2:
    print(f'o time campeão foi o {time1}')
elif gols_time2 > gols_time1:
    print(f'o time campeão foi o {time2}')
else:
    print('o resultado foi empate!')