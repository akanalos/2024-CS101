import sys
sys.setrecursionlimit(1<<30)
def compare(x):
    return x.ljust(22,x[0])
m=int(input())
n=int(input())
x=sorted(list(map(str,input().split())),reverse=True,key=compare)
length=[0]*n
used=[0]*n
mark=[]
l=0
for i in range(n):
    length[i]=len(x[i])
    if l+len(x[i])<=m:
        l+=len(x[i])
        mark.append(i)
        used[i]=1
ans=(l,mark[:])
def measure():
    global l,m,ans
    if l==m:
        return
    if mark[0]>=n-2:
        return          #剪枝
    s=mark.pop()
    l-=length[s]
    for j in range(s+1,n):
        if l+length[j]<=m:
            l+=length[j]
            mark.append(j)
            used[j]=1
            if l==m:
                ans=(m,mark[:])
                return
    if l>ans[0]:
        ans = (m, mark[:])
    measure()
    return
measure()
word=''
for ele in ans[1]:
    word=word+x[ele]
print(word)