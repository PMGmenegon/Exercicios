dicionario = {'nome' : '', 'sexo': '', 'idade' : ''}
lista = []
while True:
    dicionario['nome'] = str(input('Digite seu nome: '))
    dicionario['sexo'] = str(input('Digite seu sexo (F ou M): ')).upper()
    dicionario['idade'] = int(input('Digite sua idade: '))
    lista.append(dicionario.copy())
    continuar = str(input('Quer continuar? (S OU N) ')).lower()
    if continuar == 'n':
        break
pessoas = len(lista)
total = 0
media = 0
contador = 0
mulheres = []
for c in range(0,len(lista)):
    total += lista[c]['idade']
    if lista[c]['sexo'] == 'F':
        mulheres.append(lista[c]['nome'])
media = total / (len(lista))
for c in range(0,len(lista)):
    if lista[c]['idade'] > media:
        contador+=1
print(pessoas)
print(media)
print(contador)
print(mulheres)
    
