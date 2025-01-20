import sys
sys.setrecursionlimit(1<<30)
x=int(input())
a=[1,2]
if x>=3:
    for i in range(x-2):
        a.append(a[-1]+a[-2])
    print(a[-1])
else:
    print((a[x-1]))