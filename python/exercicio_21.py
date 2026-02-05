valor = int(input('Digite o valor da casa em reais: '))
salario = float(input('Digite o seu salário em reais: '))
anos = float(input('Digite em quantos anos você quer pagar a casa: '))
prestação = valor / (anos * 12)
if(prestação > salario * 0.3):
    print(f'Empréstimo negado, pois a prestação {prestação:.2f} excede em 30% do seu salário.')
else:
    print(f'Empréstimo aprovado! A prestação mensal será de {prestação:.2f} reais.')