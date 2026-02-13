sexo = str(input('Digite seu sexo (M ou F):')).upper()
while sexo != 'M' and sexo != 'F':
    print('Esse sexo não existe!')
    sexo = str(input('Digite seu sexo (M ou F):')).upper()
print('Sexo registrado com sucesso!')
