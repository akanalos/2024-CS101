n,k = map(int, input().split())
a=sorted(list(map(int,input().split())),reverse=True)
s=sum(a)
ans=s/k
if k==1:
    print(f'{s:.3f}')
elif n==k:
    print(f'{a[-1]:.3f}')
else:
    for i in range(k-1):
        if a[i]<=(s-a[i])/(k-1-i):
            s-=a[i]
            continue
        else:
            ans=(s-a[i])/(k-1-i)
            s-=a[i]
    print(f'{ans:.3f}')