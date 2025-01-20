# pylint: skip-file
import sys
sys.setrecursionlimit(1<<30)

dx=[0,0,1,-1]
dy=[1,-1,0,0]
def dfs(x,y,h):
    global martix,water,s,r
    if water[s][r]==1:
        return

    if water[x][y]==0:
        if h>martix[x][y]:
            water[x][y]=1
            for i in range(4):
                dfs(x+dx[i],y+dy[i],h)
            return
        else:
            return
    else:
        return
#输入时按照水位从高到低进行排序从而优化
for j in range(int(input())):
    save=[]
    m,n=map(int,input().split())
    martix=[[2000 for _ in range(n+2)] for _ in range(m+2)]
    water=[[0 for _ in range(n+2)] for _ in range(m+2)]
    for p in range(1,m+1):
        martix[p][1:-1]=list(map(int,input().split()))
    s,r= map(int, input().split())
    p=0
    q=int(input())
    while p<q:
        u=input()
        if u=='':
            continue
        else:
            p+=1
        x,y= map(int, u.split())
        if x==s and y==r:
            water[s][r]=1
        if martix[x][y]>martix[s][r]:
            save.append([x,y,int(martix[x][y])])
    save=sorted(save,key=lambda q:q[2],reverse=False)
    while save:
        a,b,c=save.pop()
        martix[a][b]-=1
        dfs(a,b,c)
        water[a][b]=1
        martix[a][b]+=1
    if water[s][r]==0:
        print("No")
    else:
        print('Yes')