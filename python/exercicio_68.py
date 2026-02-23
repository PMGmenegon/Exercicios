expressao = str(input('Digite uma expressão matemática: '))
m = expressao.count('(')
n = expressao.count(')')
if (m + n) % 2 == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')
