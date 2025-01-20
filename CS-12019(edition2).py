
# pylint: skip-file
import sys
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def dfs(x, y, h):
    global martix, water, s, r
    if water[s][r] == 1:
        return

    if water[x][y] == 0:
        if h > martix[x][y]:
            water[x][y] = 1
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                dfs(nx, ny, h)
            return
        else:
            return
    else:
        return

# 从标准输入读取所有数据
input_data =sys.stdin.read().split()
idx=1
for j in range(int(input_data[0])):
    save = []
    m=int(input_data[idx])
    n=int(input_data[idx+1])
    idx+=2
    martix = [[2000 for _ in range(n+2)] for _ in range(m+2)]
    water = [[0 for _ in range(n+2)] for _ in range(m+2)]

    for p in range(1, m+1):
        martix[p][1:-1] = list(map(int,input_data[idx:idx+m]))
        idx+=m
    s = int(input_data[idx])
    r = int(input_data[idx + 1])
    idx+=2
    u=idx
    idx+=1
    for p in range(int(input_data[u])):
        x = int(input_data[idx])
        y = int(input_data[idx + 1])
        idx+=2
        if martix[x][y] > martix[s][r]:
            save.append([x, y, int(martix[x][y])])

    save = sorted(save, key=lambda q: q[2], reverse=False)

    while save:
        a, b, c = save.pop()
        martix[a][b] -= 1
        dfs(a, b, c)
        water[a][b] = 1
        martix[a][b] += 1

    if water[s][r] == 0:
        print("No")
    else:
        print('Yes')