# pylint: skip-file
from collections import deque
from functools import lru_cache


@lru_cache(maxsize=1024)
def read():
    global n,martix,ans,m,visited
    n,m=map(int,input().split())
    martix =[[0 for _ in range(m)] for _ in range(n)]
    visited=[[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        martix[i]=list(map(int,input().split()))


@lru_cache(maxsize=1024)
def ski(start):
    global ans,visited
    ans=0
    pq=deque()
    pq.append((start,0))
    distance=[[0 for _ in range(m)] for _ in range(n)]
    while pq:
        ((x,y),d)=pq.popleft()
        if d<distance[x][y]:
            continue
        else:
            d+=1
            distance[x][y]=d
            visited[x][y]=1
            ans=max(ans,d)
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if 0<=x+dx<n and 0<=y+dy<m:
                if martix[x][y]>martix[x+dx][y+dy]:
                    pq.append(((x+dx,y+dy),d))
    return ans
read()
a=0
for i in range(n):
    for j in range(m):
        if visited[i][j]==0:
            a=max(ski((i,j)),a)
print(a)