idade = int(input('Digite quantos anos você tem: '))
if(idade<18):
    falta = 18 - idade
    print(f'Alistamento só daqui a {falta} anos.')
elif(idade>18):
    excedente = idade - 18
    print(f'Você deveria ter se alistado já há {excedente} anos.')
else:
    print('Idade certa para se alistar. Se aliste!')