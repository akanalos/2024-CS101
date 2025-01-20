import sys
sys.setrecursionlimit(1<<30)
def newsort(n,a,tem,used,x):
    if a==n:
        print(' '.join(tem))
    if tem == list(map(str,range(n, 0, -1))):
        sys.exit()
    for i in range(x,n+1):
        if i==n:
            y=int(tem.pop())
            used[y-1]=0
            newsort(n,a-1,tem,used,y)
        elif used[i]==0:
            tem.append(str(i+1))
            used[i]=1
            newsort(n,a+1,tem,used,0)
        else:
            continue

n=int(input())
tem=[]
used=[0]*n
x=0
a=0
newsort(n,a,tem,used,x)