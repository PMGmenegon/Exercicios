import random
numeros = (random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100))
print(f'{numeros}')
print(f'Maior = {sorted(numeros)[4]}\nMenor = {sorted(numeros)[0]}')