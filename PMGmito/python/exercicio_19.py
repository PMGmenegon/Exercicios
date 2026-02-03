salario = float(input('Digite o salário do funcionário: '))
if salario <= 1250:
    salario_novo = salario * 1.15
    print(f'O novo salário é {salario_novo:.2f} reais')
else:
    salario_novo2 = salario * 1.10
    print(f'O novo salário é {salario_novo2:.2f} reais')