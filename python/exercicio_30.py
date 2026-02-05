import random
novamente = True
while novamente:
    jogada = str(input('Escolha entre pedra, papel ou tesoura: ')).lower().strip()
    opções = ['pedra', 'papel', 'tesoura']
    computador = random.choice(opções)
    if jogada == computador:
        print('Empate, jogue novamente!')
    elif (jogada == 'pedra' and computador == 'tesoura') or (jogada == 'papel' and computador == 'pedra') or (jogada == 'tesoura' and computador == 'papel'):
        print(f' {jogada} x {computador}. {jogada} vence, parabéns!!! ')
        novamente = False
    else:
        print(f' {jogada} x {computador}. {computador} vence, tente novamente!!! ')