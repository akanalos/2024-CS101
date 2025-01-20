def bfs(x,y,step):
    if martix[x][y]=='2':
        return
    if fast[x][y]<=step:
        return
    else:
        fast[x][y]=step
        step+=1
    for i in range(4):
        bfs(x+dx[i],y+dy[i],step)

dx=[0,0,1,-1]
dy=[1,-1,0,0]
m,n=map(int,input().split())
martix=[['2' for _ in range(n+2)] for _ in range(m+2)]
fast=[[4000 for _ in range(n+2)] for _ in range(m+2)]
for i in range(1,m+1):
    martix[i][1:-1]=input().split()
bfs(1,1,0)
for x in range(1,m+1):
    for y in range(1, n + 1):
        if martix[x][y]=='1':
            if fast[x][y]!=4000:
                print(fast[x][y])
            else:
                print('NO')
            break