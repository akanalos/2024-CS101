x,y=map(int,input().split())
a=list(map(int,input().split()))
a=sorted(a,reverse=False)
ans=0
for i in range(y):
    if a[i]<0:
        ans-=a[i]
    else:
        break
print(ans)