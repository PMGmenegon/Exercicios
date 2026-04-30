dicionario = {'nome': '', 'partidas': '', 'g_p': '', 'totalgols': ''}
dicionario['nome'] = str(input('Digite o nome do jogador: '))
dicionario['partidas'] = int(input('Digite o número de jogos do jogador: '))
dicionario['totalgols']= 0
lista = []
for c in range(0,dicionario['partidas']):
    lista.append(int(input('Digite quantos gols o jogador fez na partida: ')))
    dicionario['totalgols']+=lista[c]
dicionario['g_p'] = lista
print(dicionario)