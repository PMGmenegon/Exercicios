pt = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razão da PA: '))
contador = 1
continua = True
while contador <= 10:
    print(f'{pt}')
    pt += razao
    contador += 1
mais = str(input('Você quer ver mais termos? (S/N)')).upper()
if mais == 'S':
    while continua:
        adicional = int(input('Quantos termos você quer ver a mais? '))
        if adicional != 0:
            total = contador + adicional
            while contador < total:
                print(f'{pt}')
                pt += razao
                contador += 1
        else:
            continua = False
print('Programa finalizado!')
