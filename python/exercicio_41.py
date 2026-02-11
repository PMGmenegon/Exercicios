media = 0
soma= 0
contador = 0
maior = 0
for c in range(0,4):
    nome = str(input('Digite um nome: '))
    idade = int(input('Digite uma idade: '))
    sexo = str(input('Digite um sexo(feminino ou masculino): '))
    soma += idade
    if idade > maior and sexo == 'masculino':
        maior = idade
        mais_velho = nome
    if sexo == 'feminino' and idade < 20:
        contador += 1
media = soma / 4
print(f'Média de idade do grupo: {media} anos\nHomem mais velho: {mais_velho}\nQuantidade de mulheres com menos de 20 anos: {contador}')