n,m=map(int,input().split())
stu=sorted(list(map(int,input().split())),reverse=False)
d=[]
ans=0
for i in range(n-1):
    d.append(stu[i+1]-stu[i])
d=sorted(d,reverse=True)
for j in range(m-1):
    ans+=d[j]
print(stu[-1]-stu[0]-ans)