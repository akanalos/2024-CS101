x=int(input())
a=list(map(int,input().split()))
ans='YES'
for i in range(x-1):
    if a[i]>a[i+1]:
        ans='NO'
print(ans)