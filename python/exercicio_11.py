frase = str(input('Digite uma frase: ')).strip()
frase_minuscula = frase.lower()
print(f'A letra A aparece {frase_minuscula.count('a')} vezes na frase\n a primeira letra a aparece na posição {frase_minuscula.find("a")+1}\n a última letra a aparece na posição {frase_minuscula.rfind("a")+1}')
