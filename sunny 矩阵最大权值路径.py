# pylint: skip-file
dx=[1,-1,0,0]
dy=[0,0,1,-1]
pat=[]
def dfs(x,y,rank):
    global his,vis,martix,n,m,ans,pat
    if x==n and y==m:
        rank += martix[x][y]
        if rank>=ans:
            pat=his[:]
            ans=rank
            rank -= martix[x][y]
            return
        else:
            rank -= martix[x][y]
            return
    if vis[x][y]==1:
        return
    else:
        vis[x][y]=1
        rank+=martix[x][y]
        for i in range(4):
            his.append(i)
            dfs(x+dx[i],y+dy[i],rank)
            his.pop()
        vis[x][y]=0
        rank-=martix[x][y]
        return
n,m=map(int,input().split())
ans=-10000000
vis=[[1 for _ in range(m+2)] for _ in range(n+2)]
his=[]
martix=[[0 for _ in range(m+2)] for _ in range(n+2)]
for i in range(1,n+1):
    martix[i][1:-1]=list(map(int,input().split()))
    vis[i][1:-1]=[0]*m
dfs(1,1,0)
print(1,1)
x=1
y=1
for ele in pat:
    x+=dx[ele]
    y+=dy[ele]
    print(x,y)