primo = int(input('Digite um número inteiro: '))
if primo > 2:
    for c in range(2, primo):
        if primo % c == 0:
            print('Não é primo')
            break
    else:
        print('É primo')
else:
    print('Não é primo')