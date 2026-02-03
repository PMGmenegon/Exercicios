velocidade = int(input('Digite a velocidade do carro em km/h:'))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você está muito rápido! Multa no valor de {multa} reais.')
else:
    print('Continue dirigindo de forma segura!')
