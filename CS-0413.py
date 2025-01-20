# pylint: skip-file
dx=[1,1,-1,-1,2,2,-2,-2]
dy=[2,-2,2,-2,1,-1,1,-1]
def dfs(x,y,step):
    global ans,martix,m,n
    if martix[x][y]==0:
        return
    else:
        step+=1
        if step==m*n:
            ans+=1
            step-=1
            return
        martix[x][y]=0
        for i in range(8):
            dfs(x+dx[i],y+dy[i],step)
        martix[x][y]=1
        step-=1
        return
for _ in range(int(input())):
    ans=0
    n,m,a,b=map(int,input().split())
    movehistory=[]
    martix=[[0]*(m+4)]+[[0]*(m+4)]+[[0,0]+[1 for _ in range(2,m+2)]+[0,0] for _ in range(2,n+2)]+[[0]*(m+4)]+[[0]*(m+4)]
    dfs(a+2,b+2,0)
    print(ans)