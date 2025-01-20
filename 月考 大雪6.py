n=int(input())
a,b=map(int,input().split())
mi=[0]*n
ans=0
tot=a
if n==0:
    print(0)
else:
    for i in range(n):
        t=list(map(int,input().split()))
        mi[i]=t[:]+[t[0]*t[1]][:]
    mi=sorted(mi,key=lambda u:(u[2],u[1],u[0]),reverse=False)
    for i in range(n-1):
        tot = tot * mi[i][0]
    ans=tot//mi[-1][1]
    print(int(ans))