numeros = list()
numerosp = list()
numerosi = list()
for c in range(0,7):
    numeros.append(int(input('Digite um número inteiro:')))
    if numeros[0] % 2 == 0:
        numerosp.append(numeros[:])
        numeros.clear()
    else:
        numerosi.append(numeros[:])
        numeros.clear()
numerosp.sort()
numerosi.sort()
print(f'{numerosp}\n{numerosi}')