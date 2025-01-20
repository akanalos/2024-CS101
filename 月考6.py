n=int(input())
a=[]
p=[0]*61
ans=0
s=-1
for i in range(n):
    a.append(list(map(int,input().split())))
a=sorted(a,key=lambda u:(u[1],100-u[0]),reverse=False)
x=len(a)
for i in range(x):
    if a[i][0]>s:
        s=a[i][1]
        ans+=1
print(ans)
