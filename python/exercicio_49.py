n = int(input('Digite até qual elemento da sequência de Fibonacci você quer ver: '))
contador = 3
elemento1 = 0
elemento2 = 1
if n == 1:
    print(f'{elemento1}')
elif n == 2:
    print(f'{elemento1}\n{elemento2}')
while contador <= n:
    elemento3 = elemento1 + elemento2
    print(f'{elemento3}')
    elemento1 = elemento2
    elemento2 = elemento3
    contador += 1
print('Sequência finalizada!')
