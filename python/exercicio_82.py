def vota(ano):
    if ano < 16:
        return 'VOTO NEGADO'
    elif (ano >=16 and ano < 18) or ano > 70:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'
nascimento = int(input('Digite o ano em que você nasceu: '))
idade = 2026 - nascimento
print(vota(idade))