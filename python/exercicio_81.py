import random
lista = []
def sorteia():
    for c in range(0,5):
        lista.append(random.randint(-10,10))
    print(lista)
def somaPar():
    soma = 0
    for elemento in lista:
        if elemento % 2 == 0:
            soma+=elemento
    print(soma)
sorteia()
somaPar()