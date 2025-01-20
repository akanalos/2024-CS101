l=[0]
s=1
t,k=map(int,input().split())
ans=[0]
u=0
while s<100005:
    if s<k:
        l.append(1)
    elif s==k:
        l.append(2)
    else:
        l.append((l[-1]+l[-k])%1000000007)
    s+=1
    u+=l[-1]
    u=u%1000000007
    ans.append(u)
for j in range(t):
    a,b= map(int, input().split())
    print((ans[b]-ans[a-1])%1000000007)