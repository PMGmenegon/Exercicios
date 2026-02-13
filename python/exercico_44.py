numero1 =  float(input('Digite um número: '))
numero2 =  float(input('Digite outro número: '))
operação = int(input('Digite a operação que deseja realizar: \n1 - Soma\n2 - Multiplicação\n3 - Maior número\n4 - Digitar novos números\n5 - Sair\n'))
while operação != 5:
    if operação == 1:
        print(f'{numero1} + {numero2} = {numero1 + numero2}')
    elif operação == 2:
        print(f'{numero1} x {numero2} = {numero1 * numero2}')
    elif operação == 3:
        if numero1 > numero2:
            print(f'O maior número é {numero1}')
        elif numero2 > numero1:
            print(f'O maior número é {numero2}')
        else:
            print('Os números são iguais')
    elif operação == 4:
        numero1 =  float(input('Digite um número: '))
        numero2 =  float(input('Digite outro número: '))
    else:
        print('Opção inválida, tente novamente')
    operação = int(input('Digite a operação que deseja realizar: \n1 - Soma\n2 - Multiplicação\n3 - Maior número\n4 - Digitar novos números\n5 - Sair'))
print('Programa encerrado, obrigado por usar!')