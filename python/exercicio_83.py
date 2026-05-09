def fatorial(num, show=False):
    if show == True:
        for c in range (num,0,-1):
            if c == num:
                continue
            else:
                num*=c
                print(f' {num}')
    else:
        for c in range (num,0,-1):
            if c == num:
                continue
            else:
                num *= c
        print(num)
fatorial(5, True)