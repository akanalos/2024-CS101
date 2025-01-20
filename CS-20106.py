import heapq
from heapq import heappush
def bfs(start,end,martix):
    visited=[[False for _ in range(n)]for _ in range(m)]
    distance=[[float('inf') for _ in range(n)]for _ in range(m)]
    distance[start[0]][start[1]]=0
    pq=[(0,start)] #(cost,position)
    while pq:
        cost,(x,y)=heapq.heappop(pq)
        if visited[x][y]:
            continue
        visited[x][y]=True
        if (x,y)==end:
            return cost
        else:
            for (dx,dy) in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx=x+dx
                ny=y+dy
                if 0<=nx<m and 0<=ny<n and not visited[nx][ny] and martix[nx][ny]!='#':
                    d=abs(martix[x][y]-martix[nx][ny])+cost
                    if d<distance[nx][ny]:
                        distance[nx][ny]=d
                        heappush(pq,(d,(nx,ny)))
    return 'NO'
def mainpart():
    global m, n
    m,n,p=map(int,input().split())
    martix = [[0 for _ in range(n)] for _ in range(m)]
    printlist=[]
    for i in range(m):
        martix[i]=list(map(lambda u:u if u=='#' else int(u),input().split()))
    for i in range(p):
        solvelist=list(map(int,input().split()))
        (sx,sy),(ex,ey)=(solvelist[0],solvelist[1]),(solvelist[2],solvelist[3])
        if martix[sx][sy]=='#' or martix[ex][ey]=='#':
            printlist.append('NO')
        else:
            printlist.append(bfs((sx,sy),(ex,ey),martix))
    print('\n'.join(str(ele) for ele in printlist))
mainpart()