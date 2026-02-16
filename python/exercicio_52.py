contador = 0
soma = 0
while True:
    numero = int(input('Digite um valor inteiro e 999 se quiser parar: '))
    if numero != 999:
        contador+=1
        soma+=numero
    else:
        break
print(f'{contador} numeros\nsoma = {soma}')
    