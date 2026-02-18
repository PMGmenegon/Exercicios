tabela = ('Caderno', 30, 'Computador', 890, 'Tênis', 270, 'Bola de futebol', 90)
for c in range(0,8,2):
    print(f'Produto: {tabela[c]}.............R$: {tabela[c+1]}')