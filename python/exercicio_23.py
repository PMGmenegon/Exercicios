valor1 = int(input('Digite um número inteiro: '))
valor2 = int(input('Digite outro número inteiro: '))
if(valor1>valor2):
    print(f'{valor1} é maior que {valor2}')
elif(valor2>valor1):
    print(f'{valor2} é maior que {valor1}')
else:
    print('Os dois números são iguais')