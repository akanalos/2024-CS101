nums=int(input())
u=list(map(int,input().split()))
sumu=[0]*nums+[0]
sumu[0]=u[0]
v=[u[0]]
sumv=[0]*nums+[0]
for i in range(1,nums+1):
    sumu[i]=sumu[i-1]+u[i-1]
v=sorted(u,reverse=False)
sumv[0]=0
for i in range(1,nums+1):
    sumv[i]=sumv[i-1]+v[i-1]
m=int(input())
for x in range(m):
    t,l,r=map(int,input().split())
    if t==1:
        print(sumu[r]-sumu[l-1])
    else:
        print(sumv[r]-sumv[l-1])