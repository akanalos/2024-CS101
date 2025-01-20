a=list(map(int,input().split()))
b=[]
for num,ele in enumerate(a,start=0):
    b.append([ele,num])
b=sorted(b,key=lambda u:u[0],reverse=False)
l=len(b)
ans=0
for q in range(l):
    for p in range(l-q):
        if b[p][1]<b[l-q-1][1]:
            ans=max(-b[p][0]+b[l-q-1][0],ans)
            break
print(ans)