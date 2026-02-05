nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua outra nota: '))
if((nota1 + nota2) / 2 < 5):
    print('Reprovado')
elif((nota1 + nota2) / 2 <=6.9 and (nota1 + nota2) / 2 >=5):
    print('Recuperação')
else:
    print('Aprovado')