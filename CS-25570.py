# pylint: skip-file
import sys


def onion(martix,n):
    global ans
    if n>2:
        s=sum(martix[0])+sum(martix[-1])
        for i in range(1,n-1):
            s+=martix[i][0]+martix[i][-1]
        ans = max(ans, s)
    elif n==2:
        s=sum(martix[0]) + sum(martix[-1])
        ans = max(ans, s)
        print(ans)
        sys.exit()
    elif n==1:
        s=martix[0][0]
        ans = max(ans, s)
        print(ans)
        sys.exit()
    n-=2
    martix=[row[1:-1] for row in martix[1:-1]]
    onion(martix,n)
x=int(input())
m=[]
ans=0
for i in range(x):
    m.append(list(map(int,input().split())))
onion(m,x)
