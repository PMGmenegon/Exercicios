soma = 0
for numeros in range(1,500,2):
    print(numeros)
    if(numeros % 3 == 0):
        soma += numeros
print(f'Soma dos múltiplos de 3: {soma}')