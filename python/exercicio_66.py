valores = list()
while True:
    valores.append(int(input('Digite um número inteiro: ')))
    continuar = str(input('Você quer continuar? S ou N: ')).lower()
    if continuar == 'n':
        break
print(f'{len(valores)} elementos digitados')
valores.sort(reverse=True)
print(valores)
if '5'in valores:
    print('5 está na lista')
else:
    print('5 não está na lista')