numero = int(input('Digite um número que você quer saber seu fatorial: '))
multiplicador = numero - 1
while multiplicador > 0:
    numero *= multiplicador
    multiplicador -= 1
print(f'O fatorial é {numero}')