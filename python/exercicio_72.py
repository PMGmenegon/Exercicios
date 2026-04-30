dicionario = {'nome' : '', 'media' : '', 'situaçao': ''}
dicionario['nome'] = str(input('Digite seu nome:'))
dicionario['media'] = float(input("Digite sua média: "))
if dicionario['media'] >= 7:
    dicionario['situaçao'] = 'aprovado'
else:
    dicionario['situaçao'] = 'reprovado'
print(dicionario.items())
