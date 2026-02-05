ano = int(input('Digite seu ano de nascimento: '))
categoria = 2026 - ano
if(categoria<=9):
    print('Mirim')
elif(categoria<=14):
    print('Infantil')
elif(categoria<=19):
    print('Júnior: ')
elif(categoria==20):
    print('Sênior')
else:
    print('Master')