nums=int(input())
u=list(map(int,input().split()))
sumu=[0]*nums+[0]
sumu[0]=u[0]
v=[u[0]]
sumv=[0]*nums+[0]
def findloc(x,tarlist):#即将进行升序排列
    length=len(tarlist)
    left,right=0,length-1
    if tarlist[0]>=x:
        return 0
    elif tarlist[-1]<x:
        return length
    while True:
        mid=(left+right)//2
        if tarlist[mid]>x:
            right=mid
        elif tarlist[mid]<=x:
            left=mid
        if right-left==(1 or 0):
            return right
            break
for i in range(1,nums+1):
    sumu[i]=sumu[i-1]+u[i-1]
    a=findloc(u[i-1],v)
    if i>1:
        v.insert(a,u[i-1])
sumv[0]=0
for i in range(1,nums+1):
    sumv[i]=sumv[i-1]+v[i-1]
m=int(input())
for x in range(m):
    t,l,r=map(int,input().split())
    if t==1:
        print(sumu[r]-sumu[l-1])
    else:
        print(sumv[r]-sumv[l-1])