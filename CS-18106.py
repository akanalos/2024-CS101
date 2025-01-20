import sys

n=int(input())
ans=[[0 for i in range(n)] for j in range(n)]
edge=[n-1,n-1,0,1]
def refresh(x,y,case,e,num):
    ans[y][x] = num
    if num==n*n:
        for i in range(n):
            print(' '.join(map(str,ans[i])))
        sys.exit()
    if case==0:
        if x!=e:
            refresh(x+1,y,0,edge[0],num+1)
        else:
            edge[0]-=1
            refresh(x,y,1, edge[1], num)
    if case==1:
        if y!=e:
            refresh(x,y+1,1,edge[1],num+1)
        else:
            edge[1]-=1
            refresh(x,y,2, edge[2], num)
    if case==2:
        if x!=e:
            refresh(x-1,y,2,edge[2],num+1)
        else:
            edge[2]+=1
            refresh(x,y,3, edge[3], num)
    if case==3:
        if y!=e:
            refresh(x,y-1,3,edge[3],num+1)
        else:
            edge[3]+=1
            refresh(x,y,0, edge[0], num)
refresh(0,0,0,n,1)