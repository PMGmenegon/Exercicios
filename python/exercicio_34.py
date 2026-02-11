numero = int(input('Digite um número e veja sua tabuada: '))
resultado = 0
for c in range(0,11):
    resultado = numero * c
    print(f'{numero} x {c} = {resultado}')