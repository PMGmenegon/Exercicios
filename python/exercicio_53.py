while True:
    numero = int(input('Digite o número que você quer saber a tabuada? '))
    if numero >= 0:
        for c in range(0,11):
            print(f'{numero * c}')
    else:
        break