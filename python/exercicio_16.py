distância = float(input('Digite o quantos km terá sua viagem: '))
if distância <= 200:
    preço1 = distância * 0.5
    print(f'Valor da sua viagem é {preço1} reais.')
else:
    preço2 = distância * 0.45
    print(f'Valor da sua viagem é {preço2} reais.')