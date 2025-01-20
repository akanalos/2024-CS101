# pylint: skip-file
direction= [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
def dfs(x,y):
    global area
    if ma[x][y]=='.':
        return
    area += 1
    ma[x][y] = '.'
    for ele in direction:
        dfs(x+ele[0],y+ele[1])
for _ in range(int(input())):
    s=0
    n, m=map(int, input().split())
    ma=[['.' for _ in range(m+2)] for _ in range(n+2)]
    for i in range(1,n+1):
        ma[i][1:-1]=list(input())
    for a in range(1,n+1):
        for b in range(1,m+1):
            if ma[a][b]=='W':
                area=0
                dfs(a,b)
                s=max(area,s)
    print(s)