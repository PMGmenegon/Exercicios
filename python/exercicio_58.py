numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesste', 'dezoito', 'dezenove', 'vinte')
numero = int(input('Digite um número inteiro de 0 a 20: '))
while True:
    if numero < 0 or numero > 20:
        print('Tente novamente')
        numero = int(input('Digite um número inteiro de 0 a 20: '))
    else:
        print(f'Seu número escolhido foi {numeros[numero]}')
        break       