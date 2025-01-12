s=input()
lines=int(input())
l=[0]*lines
r=[0]*lines
count=[0]*lines
for i in range(lines):
    [l[i],r[i]]=list(map(int,input().split()))
for i in range(lines):
    for j in range(l[i],r[i]):
        if s[j]==s[j-1]:
            count[i]=count[i]+1
for i in range(lines):
    print(count[i])