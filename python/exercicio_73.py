import random
p1 = random.randint(1,6)
p2 = random.randint(1,6)
p3 = random.randint(1,6)
p4 = random.randint(1,6)
dicionario = {'r1':p1,'r2':p2,'r3':p3,'r4':p4}
lista = []
for v in dicionario.values():
    lista.append(v)
lista.sort(reverse=True)
print(lista)
print(f'Vencedor é {lista[0]}')