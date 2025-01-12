i=0
n=[]
m=[]
n1=[]
m1=[]
while True:
    n.append([0])
    n1.append([0])
    m.append([0])
    m1.append([0])
    n[i],m[i]=input().split()
    if  n[i]=='0' and m[i]=='0':
        break
    m1[i]=int(m[i])
    n1[i]=int(n[i])
    i += 1#这一部分储存所有的nm
for j in range(i):
    x0=0
    par=list(range(1,n1[j]+1))
    while True:
        if n1[j]==1:
            break
        x=(m1[j]+x0-1)%n1[j]
        par.pop(x)
        n1[j]-=1
        x0=x
    print(par[0])