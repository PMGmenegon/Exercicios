import time
def contador(inicio, fim, passo):
    for c in range(1,11):
        print(c)
        time.sleep(1)
    for j in range(10,-1,-2):
        print(j)
        time.sleep(2)
    for k in range(inicio,fim,passo):
        print (k)
        time.sleep(passo)
contador(1,22,5)