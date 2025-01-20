x=int(input())
a=[]
b=[]
for i in range(x):
    c=list(input().split())
    if int(c[1])>=60:
        a.append(c[:])
    else:
        b.append(c[:])
a=sorted(a,key=lambda p:int(p[1]),reverse=True)
for ele in a:
    print(ele[0])
for ele in b:
    print(ele[0])