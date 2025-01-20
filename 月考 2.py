n,m1,m2=map(int,input().split())
a=[]
b=[]
c=[]
d=[0]*n
for i in range(n):
    a.append(d[:])
    b.append(d[:])
    c.append(d[:])
for i in range(m1):
    x,y,k=map(int,input().split())
    a[x][y]=k
for i in range(m2):
    x, y, k = map(int, input().split())
    b[x][y] = k
for i in range(n):
    for j in range(n):
        s = 0
        for k in range(n):
            s+=a[i][k]*b[k][j]
        if s!=0:
            print(i,j,s)