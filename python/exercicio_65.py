valores = list()
while True:
    numero = int(input('Digite um número inteiro: '))
    if numero not in valores:
        valores.append(numero)
    else:
        break
valores.sort()
print(valores)