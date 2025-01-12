h=float(input())
m=int(input())
s=[]
c=[]
l=[]
t=2*h-0.5*m
def eff(x):
    return x[2]
for i in range(m):
    a,b=map(float,input().split())
    c=a*b
    l.append([a,b,c])
l=sorted(l,key=eff,reverse=True)
ans=0
i=0
while i<m and t!=0:
    if l[i][0]*t>5:
        ans += 5*l[i][1]
        t -= 5 / l[i][0]
        i += 1
    else:
        ans += l[i][2] * t
        t = 0
    if i == m:
        break
print(f'{ans:.1f}')