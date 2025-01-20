*values,=map(int,input().split(','))
ans,s0,s1=0,0,0
l=len(values)
for i in range(l):
    s1=max(s0,s1+values[i])
    s0=max(values[i],s0+values[i])
    ans=max(ans,s1,s0)
if max(values)<0:
    print(max(values))
else:
    print(ans)