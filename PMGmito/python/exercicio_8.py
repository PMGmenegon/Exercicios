n = int(input('Digite um número inteiro entre 0 e 9999: '))
n_str = str(n)
print(f'Analisando o número {n} ele tem:\nUnidads: {n_str[3]}\nDezenas: {n_str[2]}\nCentenas: {n_str[1]}\nMilhares: {n_str[0]}')