s=input()
lines=int(input())
l=[0]*lines
r=[0]*lines
x=0
for i in range(lines):
    [l[i],r[i]]=list(map(int,input().split()))
le=len(s)
count=[0]*le
c=0
for i in range(1,le):
    if s[i]==s[i-1]:
        c+=1
    count[i]=c
for i in range(lines):
    print(-count[l[i]-1]+count[r[i]-1])