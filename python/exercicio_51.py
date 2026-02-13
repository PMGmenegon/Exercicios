numero = int(input('Digite um número inteiro: '))
contador = 0
soma = 0
continua = True
maior = numero
menor = numero
while continua:
    contador += 1
    soma += numero
    if numero> maior:
        maior = numero
    if numero < menor:
        menor = numero
    laço = str(input('Quer continuar? (S/N)')).upper()
    if laço == 'S':
        numero = int(input('Digite um número inteiro: '))
    elif laço == 'N':
        continua = False
media = soma / contador
print(f'média = {media}\nmaior = {maior}\nmenor = {menor}')