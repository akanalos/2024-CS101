a,b,c=[],[],[]
x=int(input())
for i in range(0,x):
    sav=list(map(int,input().split()))
    a.append(sav[0])
    b.append(sav[1])
    c.append(sav[2])
dir1=sum(a)
dir2=sum(b)
dir3=sum(c)
if dir1==0 and dir2==0 and dir3==0:
    print('YES')
else:
    print('NO')