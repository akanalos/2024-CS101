#solution
#首先对过远的岛进行检索，看是否输出-1
#接下来进行y轴排序
#对每个点被覆盖需要的雷达站选址进行记录，现在我们得到了一堆左右端值列表site，状态列表cov
#从最左端值开始向最右端值“遍历”
#每个雷达站设立在最小的右端值位置，然后覆写掉可以被覆盖的岛屿。
#注意到x/y坐标是有可能相同的
from math import sqrt
count=0

while True:
    n, r = map(int, input().split())
    pos = []
    ans = 0
    if n==0 and r==0:
        break
    else:
        count+=1
    for i in range(n):
        x,y=map(int,input().split())
        if y>r:
            ans=-1
        else:
            d=sqrt(r*r-y*y)
            pos.append([x-d,x+d])
    signal = input()
    if ans==-1:
        print(f'Case {count}: {ans}')
        continue
    else:
        pos=sorted(pos,key=lambda x:(x[1],x[0]),reverse=False)
        l=len(pos)
        cov=[True]*l
        for i in range(n):
            if cov[i]:
                ans+=1
                j=0
                cov[i]=False
                while True:
                    if i+j==l-1:
                        break
                    j+=1
                    if cov[i+j]:
                        if pos[i+j][0]<=pos[i][1]:
                            cov[i+j]=False
                    if pos[i+j][0]>pos[i][1]+r:
                        break
    print(f'Case {count}: {ans}')
