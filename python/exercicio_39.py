contador1 = 0
contador2 = 0
for c in range(0,7):
    idade= int(input('Digite uma idade: '))
    if idade >= 18:
        contador1 += 1
    else:
        contador2 += 1
print(f'{contador1} pessoas maiores idade\n{contador2} pessoas menores de idade')