contador = 0
soma = 0
valor = None
print('Bem vindo ao analisador de produtos')
while True:
    nome = str(input('Digite o produto: '))
    preço = float(input('Digite seu preço: '))
    soma+=preço
    if preço>1000:
        contador+=1
    if preço<=valor or valor is None:
        valor = preço
        cheapest = nome
    escolha = str(input('Quer continuar? ')).upper()
    if escolha == 'NÃO':
        break
print(f'{soma} reais gastos\n{contador} produtos mais caros que 1000 reais\n{cheapest} produto mais barato')