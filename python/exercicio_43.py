import random
palpite = int(input('Digite um número entre 0 e 10: '))
contador = 0
resposta = random.randint(0,10)
while palpite != resposta:
    palpite = int(input('Tente novamente: '))
    contador += 1
print(f'Parabéns e o número era {resposta}\nVocê acertou com {contador} tentativas')