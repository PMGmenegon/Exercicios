nome = str(input('Digite seu nome completo: '))
dividido = nome.split()
print(f'Muito prazer em te conhecer, meu brother!\nSeu primeiro nome é {dividido[0]}\nSeu último nome é {dividido[len(dividido)-1]}')
#Como não tratei com strip tem que ser certo os espaços.