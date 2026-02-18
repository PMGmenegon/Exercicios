palavras_sem_acento = ('messi', 'botafogo', 'renata', 'maria', 'eduarda')
for c in palavras_sem_acento:
    print(f'Na palavra {c} temos: ')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(f'{letra}')