x=int(input())
a=list(map(int,input().split()))
a=sorted(a,reverse=True)
tot=sum(a)
ur=0
i=0
while ur<=tot/2:
    ur+=a[i]
    i+=1
print(i)