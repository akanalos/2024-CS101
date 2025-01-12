import copy
while True:
    n=int(input())
    if n!=0:
        keys = list(map(int, input().split()))
        s = keys[:]
        t = 0
        o=0
        c = [keys[:]]
        while True:
            for j in range(n):
                s[j]=c[o][keys[j]-1]
            c.append(s[:])
            t+=1
            o+=1
            if c[o]==keys:
                break
        s.clear()
        while True:
            x = input()
            if x == '0':
                break
            k,x=map(str,x.split(' ',1))
            k=int(k)%t-1
            save1 = [' '] * n
            l=len(x)
            for j in range(l):
                save1[c[k][j]-1] = x[j]
            x = save1[:]
            save1.clear()
            print(''.join(x))
        c.clear()
    else:
        break
print()