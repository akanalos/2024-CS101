def refresh(x:list,a,b)->int:
    ans=0
    for n1 in range(a-1, a+2):
        for n2 in range(b-1,b+2):
            ans+=x[n1][n2]
    if x[a][b]==1 and 3<=ans<=4:
        return 1
    elif x[a][b]==0 and ans==3:
        return 1
    else:
        return 0
n,m=map(int,input().split())
cell=[0]*(n+2)
new=[0]*(n)
for i in range(n):
    cell[i+1]=[0]+list(map(int,input().split()))+[0]
    new[i]=[0]*m
cell[0]=(m+2)*[0]
cell[n+1]=(m+2)*[0]
for n1 in range(n):
    for n2 in range(m):
        new[n1][n2]=refresh(cell,n1+1,n2+1)
for n1 in range(n):
    print(' '.join(map(str,new[n1])))