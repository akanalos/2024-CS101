import sys

l,n,m=map(int,input().split())
d=[0]
def check(x):
    count=0
    pos=0
    global m,l
    for j in range(n+1):
        if d[j]-pos>=x:
            pos=d[j]
            count+=1
    if l-pos>=x:
        count+=1
    if n+1-count<=m:
        return True
    else:
        return False
for i in range(n):
    d.append(int(input()))
start=0
end=l+1
while end-start>4:
    if check((end+start)//2):
        start=(end+start)//2
    else:
        end=(end+start)//2+2
for q in range(end,start-1,-1):
    if check(q):
        print(q)
        sys.exit()