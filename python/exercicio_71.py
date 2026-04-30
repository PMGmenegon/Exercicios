matriz = []
for c in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input('Digite um número inteiro: ')))
    matriz.append(linha)
for c in range(3):
    for j in range(3):
        print(f'{matriz[c][j]}', end=' ')
    print()