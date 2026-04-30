grupo = list()
pp = list()
pessoas = 0
while True:
    grupo.append(str(input('Digite o nome da pessoa: ')))
    grupo.append(int(input('Digite seu peso apenas em quilos: ')))
    pp.append(grupo[:])
    grupo.clear()
    continuar = str(input('Quer continuar? S ou N: ')).lower()
    if continuar == 'n':
        break
pesado = pp[0][1]
leve = pp[0][1]
for peso in pp:
    if peso[1] > pesado:
        pesado = peso[1]
    if peso[1] < leve:
        leve = peso[1]
    pessoas+=1
print(f'a pessoa mais pesada pesa {pesado} quilos\na pessoa mais leve pesa {leve} quilos\n{pessoas} foram cadastradas')