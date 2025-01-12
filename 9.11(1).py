i=3
x=int(input())
count=0
lis=[2]
while i<x:#找到所有指数
    for elements in lis:
        if i%elements==0:
            break
        if elements==lis[-1]:
            lis.append(i)#这样就找到了下一个质数
    i=i+2
if x<6 or x%2!=0:
    print('Error!')
else:
    while count<=len(lis):
        if x - lis[count]<lis[count]:
            break
        if x-lis[count] in lis:
            print(str(x)+'='+str(lis[count])+'+'+str(x-int(lis[count])))
        count+=1