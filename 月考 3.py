import bisect

nCases=int(input())
for p in range(nCases):
    n, m, b=map(int,input().split())
    p=[0]*n
    unused=[]
    l=0
    m0=0
    for i in range(n):
        t,x=map(int,input().split())
        p[i]=[t,x]
    t=0
    p=sorted(p,key=lambda u:(u[0],9999999999-u[1]),reverse=True)
    while len(p)>0:
        if len(unused)==0 and m0>0:
            if p[-1][0]>t:
                t+=1
                m0=m
            elif p[-1][0]==t:
                b-=p[-1][-1]
                p.pop()
                m0-=1
        elif m0==0:
            if p[-1][0]==t:
                index = bisect.bisect_left(unused, p[-1][1])
                unused.insert(index, p[-1][1])
                p.pop()
            else:
                t+=1
                m0=m
        elif len(unused)>0 and m0>0:
            m0-=1
            b-=unused.pop()
        if b<=0:
            break
    if sum(unused)<b:
        print('alive')
    else:
        while m0>0:
            b-=unused.pop()
            m0-=1
        if b<0:
            print(t)
        else:
            while b>0:
                t+=1
                for k in range(m):
                    b -= unused.pop()
            print(t)
