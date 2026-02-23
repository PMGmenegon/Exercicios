valores = list()
for numeros in range(0,5):
    valores.append(int(input('Digite um valor inteiro: ')))
maior = valores[0]
menor = valores[0]
mi = 0
mi2 = 0
for i,v in enumerate(valores):
    if v >= maior:
        maior = v
        mi = i
    if v <= menor:
        menor = v
        mi2 = i
print(f'O maior valor é {maior} que está na posição {mi}\nO menor valor é {menor} que está na posição {mi2}')