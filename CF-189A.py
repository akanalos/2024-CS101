import sys
n,a,b,c=map(int,input().split())
a,b,c=sorted([a,b,c],reverse=False)
ans=n//a
n=n%a
out=[]
if n==0:
    print(ans)
    sys.exit()
while ans>=1:
    n+=a
    ans-=1
    p=n
    ans1=ans
    while p>=0:
        if p%b==0:
            ans1+=p//b
            out.append(ans1)
            break
        else:
            p-=c
            ans1 += 1
print(max(out))