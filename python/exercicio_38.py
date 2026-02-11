frase = str(input('Digite uma frase: '))
frase_invertida = ''
for letra in range(len(frase)-1, -1, -1):
    if frase[letra] == ' ':
        continue
    else:
        frase_invertida += frase[letra]
if(frase.replace(' ', '') == frase_invertida):
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')