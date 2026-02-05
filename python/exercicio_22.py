nunero = float(input("Digite um número: "))
conversor = int(input("Digite 1 para converter para binário, 2 para octal e 3 para hexadecimal: "))
if(conversor == 1):
    print(f"O número {nunero} em binário é {bin(int(nunero))[2:]}")
elif(conversor == 2):
    print(f"O número {nunero} em octal é {oct(int(nunero))[2:]}")
elif(conversor == 3):
    print(f"O número {nunero} em hexadecimal é {hex(int(nunero))[2:]}")
else:
    print("Não existe no conversor!")