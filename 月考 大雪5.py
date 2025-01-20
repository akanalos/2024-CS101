import sys
sys.setrecursionlimit(1<<30)
dx=[0,0,1,-1]
dy=[1,-1,0,0]
island=[]
for i in range(60):
    island.append(set())
def bfs_island(x,y):
    if 0 <= x < n and 0 <= y < n:
        if martix[x][y]=='1':
            martix[x][y]='0'
            island[1].add((x,y))
            for k in range(4):
                bfs_island(x+dx[k],y+dy[k])
        return
    else:
        return
def bfs(u):
    global n
    for ele in island[u]:
        for k in range(4):
            x=ele[0]+dx[k]
            y=ele[1]+dy[k]
            if 0 <=x<n and 0<=y<n:
                if (x,y) not in island[u] and (x,y) not in island[u-1]:
                    if martix[x][y]=='1':
                        print(u-1)
                        sys.exit()
                    island[u+1].add((x,y))
    return
n=int(input())
martix=[['0' for _ in range(n)] for _ in range(n)]
for i in range(n):
    martix[i]=list(input())
for i in range(n):
    for j in range(n):
        if martix[i][j]=='1':
            bfs_island(i,j)
            for u in range(1,50):
                bfs(u)
