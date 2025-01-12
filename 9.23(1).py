x=int(input())
kid=list(map(int,input().split()))
num=len(kid)
s1=[]
s2=[]
for i in range(x):#查询本班学生状态
    if i+1 not in kid:
        s1.append(str(i+1))
for j in range(x+1,10005):#清查外班注意边界
    if j in kid:
        k=kid.count(j)
        for _ in range(k):
            s2.append(str(j))#注意外班的小可爱可能学号一样
print(f"{' '.join(s1)}")
print(f"{' '.join(s2)}")