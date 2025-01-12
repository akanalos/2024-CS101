[num,weight]=list(map(int,input().split()))
a=[0]*num
b=[0]*num
worth=[0]*num
dic={}
for i in range(num):
    [a[i],b[i]]=list(map(int,input().split()))#存储价值和重量
    worth[i]=a[i]/b[i]#单价
    if worth[i] in dic:
        p=dic[worth[i]]
        a[p]+=a[i]
        b[p]+=b[i]
        a[i]=b[i]=0
        continue
    else:
        dic[worth[i]]=i#方便之后对应
wlist=[worth[0]]
for j in range(1,num):
    k=0
    if a[j]==0:
        continue
    while worth[j]>wlist[k]:
        k=k+1
        if k==len(wlist):
            break
    wlist.insert(k,worth[j])
#现在我们有按照升序排列的wlist（对应单价），通过dic可以查询到对应的a价值、b重量编号
j=k=v=0
i=len(wlist)-1
while True:
    p=dic[wlist[i]]#反向查询编号
    if b[p]<weight:
        weight-=b[p]
        v+=a[p]#可以全部带走对应箱子
    else:
        v+=wlist[i]*weight
        weight=0#快要装不下了，剩余重量全部给对应的
        break
    i-=1
    if i==-1:
        break#防止能全部带走时陷入死循环
v=float(v)
round(v,1)
print(f"{v:.1f}"+'\n')