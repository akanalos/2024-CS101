n,m=map(int,input().split())
ans=0
island=[[0 for i in range(m+2)] for j in range(n+2)]
for i in range(n):
    island[i+1]=[0]+list(map(int,input().split()))+[0]
for i in range(0,n+1):
    for j in range(0,m+1):
        if island[i][j]==0:
            ans+=island[i+1][j]+island[i][j+1]
        else:
            ans+=2-(island[i+1][j]+island[i][j+1])
print(ans)