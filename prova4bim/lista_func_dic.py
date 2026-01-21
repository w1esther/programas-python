# ex1:

dicionario_notas = {

}

num_alunos = int(input('digite quantos alunos deseja registrar a nota: '))

for n in range(num_alunos):
    nome_aluno = input(f'digite o nome do {n+1}º aluno: ')
    nota_aluno = float(input(f'digite a nota do {n+1}º aluno: '))
    
    dicionario_notas[nome_aluno] = nota_aluno

# for nome, nota in dicionario_notas.items():
#     print(f'{nome}: {nota}')

print(dicionario_notas)

for elemento in dicionario_notas:
    valor = dicionario_notas[elemento]
    print(valor)


# ex2:

lista_numeros = []

qntd_numeros = int(input('digite quantos numeros deseja colocar na lista para que seja calculada a média desses números: '))

for i in range(qntd_numeros):
    num = float(input(f'digite o {i+1}º número: '))
    lista_numeros.append(num)

def calcular_media(lista):
    somatorio = 0
    for n in lista:
        somatorio += n
    num_elementos = len(lista)

    media_numeros = somatorio / num_elementos

    return media_numeros

media = calcular_media(lista_numeros)
print(media)

# ex 3:

lista_numeros = []

qntd_numeros = int(input('digite quantos numeros deseja colocar na lista para verificar quantos pares e ímpares há: '))

for i in range(qntd_numeros):

    num = float(input(f'digite o {i+1}º número: '))
    lista_numeros.append(num)

def verificar_par_impar(lista):

    somatorio_par = 0
    somatorio_impar = 0

    for j in lista:
        if j % 2 == 0:
            somatorio_par += 1
        else:
            somatorio_impar +=1

    dicionario_qtnd_par_impar = {

    }

    dicionario_qtnd_par_impar['quantidade de números pares'] = somatorio_par
    dicionario_qtnd_par_impar['quantidade de números ímpares'] = somatorio_impar

    return dicionario_qtnd_par_impar

num_par_impar = verificar_par_impar(lista_numeros)

print(num_par_impar)

# ex8:

qntd_notas = int(input('digite quantos alunos deseja realizar o regristro de notas: '))

dicionario_alunos = {

}
 
for k in range(qntd_notas):
    nome = input(f'digite o nome do {k+1}º aluno: ')

    lista_notas = []

    for l in range(4):
        nota = float(input(f'digite a nota do {l+1}º bimestre: '))
        lista_notas.append(nota)

    dicionario_alunos[nome] = lista_notas

def calcular_media(dicionario):

    dicionario_media = {
            
        }
    
    for elemento in dicionario:
        lista_notas2 = dicionario[elemento]

        somatorio = 0

        for p in lista_notas2:
            
            somatorio += p

        media = somatorio/4

        # dicionario_media[elemento] = media

        if media >= 6:
            dicionario_media[elemento] = 'aprovado'
        else:
            dicionario_media[elemento] = 'reprovado'
        
    return dicionario_media


calcular_media_alunos = calcular_media(dicionario_alunos)
print(calcular_media_alunos)
            
