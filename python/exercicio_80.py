def maior(*núm):
    elemento = núm[0]
    for elementos in núm:
        if elemento<elementos:
            elemento = elementos
    print(elemento)
maior(5,4,3,9,8,7,0)