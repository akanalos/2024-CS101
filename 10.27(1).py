import sys
sys.setrecursionlimit(1<<30)
n=int(input())
a=[]
def plan(m,x,target,count,mem):
    if x==n:
        a.append(count)
    elif target[x]>m:
        plan(m, x+1, target, count,mem)
    else:
        mem.append([m,x,count])
        plan(target[x],x+1,target,count+1,mem)
        m,x,count=map(int,mem.pop())
        plan(m, x + 1, target, count, mem)
target=list(map(int,input().split()))
plan(10000000000,0,target,0,[])
print(max(a))
