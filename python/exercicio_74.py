dicionario = {'nome': '', 'idade': '' , 'CTPS': '','ano de nascimento': '', 'ano_contrataçao': '', 'salario': '', 'aposentadoria': ''}
dicionario['nome'] = str(input('Digite seu nome: '))
dicionario['ano de nascimento'] = int(input('Digite seu ano de nascimento: '))
dicionario['CTPS'] = int(input("Digite o número da sua carteira de trabalho: "))
dicionario['idade'] = 2026 - dicionario['ano de nascimento']
if dicionario['CTPS']!=0:
    dicionario['ano_contrataçao'] = int(input('Digite o ano em que você foin contratado'))
    dicionario['salario'] = int(input('Digite seu salário'))
dicionario['aposentadoria'] = 65 - dicionario['idade']
for k,v in dicionario.items():
    print(f'{k} = {v}')
