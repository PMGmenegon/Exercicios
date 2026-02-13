numero = int(input('Digite um número inteiro: '))
contador = 0
soma = 0
verdade = True
while verdade:
    if numero != 999:
        soma += numero
        contador += 1
        numero = int(input('Digite um número inteiro: '))
    else:
        verdade = False
print(f'Foram digitados {contador} números e a soma entre eles é {soma}')
