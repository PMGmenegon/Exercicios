contador1 = 0
contador2 = 0
contador3 = 0
while True:
    print('Bem vindo ao sistema de cadastro!!')
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa: ')).upper()
    if sexo == 'MASCULINO':
        contador1+=1
    if idade >= 18:
        contador2+=1
    if sexo == 'FEMININO' and idade < 20:
        contador3+=1
    escolha = str(input('Quer cadastrar mais algúem? (Sim ou Não)')).upper()
    if escolha == 'NÃO':
        break
print(f'{contador1} pessoas do sexo masculino\n{contador2} maiores de idade\n{contador3} mulheres menores de 20 anos')
