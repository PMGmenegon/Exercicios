valores = list()
while True:
    valores.append(int(input('Digite um valor inteiro: ')))
    continuar = str(input('Quer continuar? S ou N: ')).lower()
    if continuar == 'n':
        break
valoresp = list()
valoresi = list()
for v in valores:
    if v % 2 == 0:
        valoresp.append(v)
    else:
        valoresi.append(v)
print(valores)
print(valoresp)
print(valoresi)