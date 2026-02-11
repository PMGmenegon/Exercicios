soma = 0
for numeros in range(0,6):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        soma += n
print(f'Soma dos números pares: {soma}')