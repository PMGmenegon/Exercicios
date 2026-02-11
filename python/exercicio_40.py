maior = 0
menor = 0
for c in range(0,5):
    peso = float(input('Digite um peso: '))
    if peso > maior:
        maior = peso
    elif peso < menor or menor == 0:
        menor = peso
print(f'Maior peso é {maior} quilos\nMenor peso é {menor} quilos.')
                 