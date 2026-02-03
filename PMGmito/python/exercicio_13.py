import random
valor = random.randint(0,5)
correto = True
while correto:
    palpite = int(input('Digite um número entre 0 e 5:'))
    if palpite == valor:
        print(f'Parabéns! Você acertou o número {valor}!')
        correto = False
    else:
        print(f'Que pena! Você errou. O número era {valor}.')