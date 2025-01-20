import sys
sys.setrecursionlimit(1<<30)
x=int(input())
a=[1]
if x>=2:
    for i in range(x-1):
        a.append(sum(a)+1)
    print(a[-1])
else:
    print(1)