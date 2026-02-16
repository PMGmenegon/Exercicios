import random
contador = 0
while True:
    escolha = str(input('Par ou impar? ')).upper()
    numero = int(input('Digite um número inteiro: '))
    adversario = random.randint(0,10)
    if escolha == 'PAR':
        if (numero + adversario) % 2 == 0:
            contador+=1
            print(f'Você ganhou {numero} mais {adversario} = {numero + adversario} ')
        else:
            print(f'Você perdeu {numero} mais {adversario} = {numero + adversario} ')
            break
    if escolha == 'IMPAR':
        if (numero + adversario) % 2 != 0:
            contador+=1
            print(f'Você ganhou {numero} mais {adversario} = {numero + adversario} ')
        else:
            print(f'Você perdeu {numero} mais {adversario} = {numero + adversario} ')
            break
print(f'Você alcançou {contador} vitórias seguidas!')