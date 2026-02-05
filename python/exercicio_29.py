preço = float(input('Digite o preço do produto em reais: R$ '))
metodo = int(input('Escolha a forma de pagamento:\n1 - À vista dinheiro/cheque\n2 - À vista cartão\n3 - 2x no cartão\n4 - 3x ou mais no cartão\nDigite a opção desejada (1-4): '))
if metodo == 1:
    desconto = preço * 0.10
    total = preço - desconto
    print(f'Pagamento à vista em dinheiro/cheque. Desconto de R$ {desconto:.2f}. Total a pagar: R$ {total:.2f}.')
elif metodo == 2:
    desconto = preço * 0.05
    total = preço - desconto
    print(f'Pagamento à vista no cartão. Desconto de R$ {desconto:.2f}. Total a pagar: R$ {total:.2f}.')
elif metodo == 3:
    total = preço
    parcela = total / 2
    print(f'Pagamento em 2x no cartão. Total a pagar: R$ {total:.2f}. 2 parcelas de R$ {parcela:.2f} sem juros.')
elif metodo == 4:
    juros = preço * 0.20
    total = preço + juros
    num_parcelas = int(input('Digite o número de parcelas (3 ou mais): '))
    parcela = total / num_parcelas
    print(f'Pagamento em {num_parcelas}x no cartão. Juros de R$ {juros:.2f}. Total a pagar: R$ {total:.2f}. {num_parcelas} parcelas de R$ {parcela:.2f}.')
else:
    print('Opção de pagamento inválida.')