i=0
a=[]
while True:
    a1=list(map(int,input().split()))
    if a1==[0]*6:
        break
    a.append(a1)#输入版块，不带0行
l=len(a)
for i in range(l):
    box = 0
    box+=a[i][-1]+a[i][-2]+a[i][-3]#4,5,6都单独占用一个
    a[i][0]-=11*a[i][-2]#5用1补齐
    if a[i][1]>=5*a[i][3]:#4优先用2补齐
        a[i][1]-=5*a[i][3]
    else:
        a[i][0]=a[i][0]-20*a[i][3]+4*a[i][1]#部分会用1补齐
        a[i][1]=0#2用完了
    if a[i][0]<0:
        a[i][0]=0#防止1*1过少在上述运算中“倒欠”
    if a[i][2]>=4:#4个3刚好拼一个
        box+=a[i][2]//4
        a[i][2]=a[i][2]%4
    if a[i][2]>0:
        box+=1
    if a[i][2]==1:#1和2完全可以只考虑总面积，但2不可与-1扯上关系
        a[i][1]-=5
        a[i][0]-=7
    if a[i][2]==2:
        a[i][1]-=3
        a[i][0]-=6
    if a[i][2]==3:
        a[i][1]-=1
        a[i][0]-=5
    if a[i][0]<0:#规避-1影响
        a[i][0]=0
    s=a[i][0]+4*a[i][1]
    if s>0:
        box+=s//36
        if s%36!=0:
            box+=1
    print(box)
    box=0