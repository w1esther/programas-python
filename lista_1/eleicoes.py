candidato1 = []
candidato2 = []

for n in range(1, 15):
    print('se você deseja votar no candidato 1 digite "1", já se você deseja votar no candidat 2 digite "2" ')
    voto = int(input('digite seu voto: '))
    if voto == 1:
        candidato1.append(voto)
    elif voto ==2:
        candidato2.append(voto)

votos_1 = len(candidato1)
votos_2 = len(candidato2)

if votos_1 > votos_2:
    print(f'o candidato 1 ganhou as eleições com {votos_1} votos dos 15')
elif votos_2 > votos_1:
    print(f'o candidato 2 ganhou as eleições com {votos_2} votos dos 15')