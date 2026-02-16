while True:
    sacado = int(input('Digite o valor inteiro que você quer sacar: '))
    notas50 = sacado // 50
    resto = sacado % 50
    notas20 = resto // 20
    resto = resto % 20
    notas10 = resto // 10
    resto = resto % 10
    notas1 = resto
    print(f'''
{notas50} notas de 50 reais
{notas20} notas de 20 reais
{notas10} notas de 10 reais
{notas1} notas de 1 real
''')
    escolha = input('Deseja sacar mais? [S/N] ').strip().upper()
    if escolha == 'N':
        break
