a,b,k=map(int,input().split())
m=[[1 for _ in range(3*b)] for _ in range(3*a)]#三倍扩充保证边界
for _ in range(k):
    x,y,p,T=map(int,input().split())
    r=int((p-1)//2)
    x=x-1#因为列表从0开始，坐标一致减一
    y=y-1
    if T==0:
        for n1 in range(max(a,a+x-r),min(a+x+r+1,2*a)):
            for n2 in range(max(b,b+y-r),min(2*b,b+y+r+1)):
                m[n1][n2]=0#碉堡不可能在范围内
    elif T==1:
        for n1 in range(a,2*a):
            for n2 in range(b,2*b):
                if a+x-r<=n1<=a+x+r and b+y-r<=n2<=b+y+r:
                    continue
                else:
                    m[n1][n2]=0#碉堡不可能在范围外
ans=0
for i in range(a,2*a):
    for j in range(b,2*b):
        ans+=m[i][j]#对所有地图内的点求和（可能点位被标注了“1”）
print(ans)