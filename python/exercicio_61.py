contador = 0
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um número inteiro: '))
n3 = int(input('Digite um número inteiro: '))
n4 = int(input('Digite um número inteiro: '))
numeros = (n1,n2,n3,n4)
print('Pares:')
for c in range(0,4):
    if numeros[c] == 9:
        contador+=1
    if numeros[c] % 2 == 0:
        print(f'{numeros[c]}')
if 3 in numeros:
    print(f'O valor 3 apareceu primeiro na posição {numeros.index(3) + 1}')
else:
    print('O 3 não faz parte da tupla!')
print(f'O número 9 apareceu {contador} vezes')