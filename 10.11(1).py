m,n,p,q=map(int,input().split())
a=[[0]*n]*m
core=[[0]*q]*p
for i in range(m):
    a[i] = list(map(int, input().split()))
for j in range(p):
    core[j] = list(map(int, input().split()))
x=n-q+1
y=m-p+1
ans=[[0]*x]*y
for j in range(y):
        ans[j]=[0]*x
for i in range(x):
    for j in range(y):
        for k in range(p):
            for l in range(q):
                u=core[k][l] * a[j + k][i + l] + ans[j][i]
                ans[j][i]=u
for i in range(y):
    print(' '.join(map(str,ans[i])))