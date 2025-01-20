import sys
martix = [[0 for _ in range(6)] for _ in range(5)]

for i in range(5):
    martix[i]=list(map(int,input().split()))
start = 0
end = 63
max_length = len(bin(end)) - 2
for i in range(start,end+1):
    measure = [[0 for _ in range(6)] for _ in range(5)]
    num=bin(i)[2:]
    order=num.zfill(max_length)
    for t in range(6):
        measure[0][t]=int(order[t])
    measure[1][0] = (measure[0][0]+martix[0][0]+measure[0][1]) % 2
    measure[1][5] = (measure[0][5]+martix[0][5]+measure[0][4]) % 2
    for y in range(1, 5):
        measure[1][y] = (measure[0][y] + measure[0][y - 1] + measure[0][y + 1] +martix[0][y]) % 2
    for x in range(2,5):
        measure[x][0]=(measure[x-1][0]+measure[x-1][1]+martix[x-1][0]+measure[x-2][0])%2
        measure[x][5]=(measure[x-1][5]+measure[x-1][4]+martix[x-1][5]+measure[x-2][5])%2
        for y in range(1,5):
            measure[x][y]=(measure[x-1][y]+measure[x-2][y]+measure[x-1][y-1]+measure[x-1][y+1]+martix[x-1][y])%2
    signal=0
    for x in range(5):
        if signal==1:
            break
        for y in range(6):
            check=0
            for (dx, dy) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if 0 <= x + dx < 5 and 0 <= y + dy < 6:
                    check+=measure[x+dx][y+dy]
            if (check+martix[x][y]+measure[x][y])%2==1:
                signal=1
                break
    if signal==1:
        continue

    for row in measure:
        print(' '.join(str(ele) for ele in row))