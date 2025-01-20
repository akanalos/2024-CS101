# pylint: skip-file
low=[]
loc=[]
while True:
    l=0
    x=input()
    if x=='':
        break
    if EOFError:
        break
    if x == 'min':
        if low:
            print(low[-1])
    elif x == 'pop':
        if low:
            l -= 1
            if l == loc[-1]:
                loc.pop()
                low.pop()

    else:
        _, n = x.split()
        int(n)
        if low:
            if n <= low[-1]:
                loc.append(l)
                low.append(n)
        else:
            loc.append(l)
            low.append(n)
        l += 1
