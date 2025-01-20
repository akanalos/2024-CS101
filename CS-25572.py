from collections import deque
crab=[]
def read():
    global n,martix,crab,end,pq,visited
    n=int(input())
    martix=[[0 for _ in range(n)] for _ in range(n)]
    visited=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        martix[i]=list(map(int,input().split()))
    for i in range(n):
        for j in range(n):
            if martix[i][j]==5:
                crab.append((i,j))
            elif martix[i][j]==9:
                end=(i,j)
def bfs(start,ed,martix):
    pq=deque()
    pq.append(((start[0],start[1])))
    while pq:
        ((x1,y1),(x2,y2))=pq.popleft()
        if visited[x1][y1] and visited[x2][y2]:
            continue
        if martix[x1][y1]==1 or martix[x2][y2]==1:
            continue
        if (x1,y1)==ed or (x2,y2)==ed:
            return 'yes'
        visited[x1][y1]=1
        visited[x2][y2]=1
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            if 0<=x1+dx<n and 0<=x2+dx<n and 0<=y1+dy<n and 0<=y2+dy<n:
                pq.append(((x1+dx,y1+dy),(x2+dx,y2+dy)))
    return 'no'
read()
print(bfs(crab,end,martix))