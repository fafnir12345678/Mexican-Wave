def wave(x):
    x=list(map(str,x))
    p=[]
    for i in range(len(x)):
        x[i]=x[i].upper()

        if x[i]!=' ':
            p.append(''.join(x))
            x[i]=x[i].lower()
    return p

print(wave('wertyu werty fgds'))
