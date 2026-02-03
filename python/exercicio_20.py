lado1 = int(input('Digite o comprimento do primeiro lado do triângulo: '))
lado2 = int(input('Digite o comprimento do segundo lado do triângulo: '))
lado3 = int(input('Digite o comprimento do terceiro lado do triângulo: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Pode ser triângulo!')
else:
    print('Não pode ser triângulo! ')