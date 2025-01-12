from math import log10, log1p
x=int(input())
need=list(map(int,input().split()))
maxn=int(max(need)**0.5)+3
num1=range(maxn)
num2=[True]*(maxn)
zlist=[]
for i in range(2,maxn):
    if num2[i]:
        zlist.append(i**2)
        for j in range(i*i,maxn,num1[i]):
            num2[j]=False
    else:
        continue
for ele in need:
    if ele**0.5==int(ele**0.5) and ele>3:
        if num2[int(ele**0.5)]:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')