x=int(input())
x1=x
count1=int(x**0.5)#避免完全遍历
count3=0#质因数统计
for i in range(2,count1+2):
    count2 = 0
    if x1==2 or x1==3 or x1==1:#（端值单独处理了）
        break
    while x%i==0:
        x=x/i
        count2+=1#当前质因数统计
    if count2%2==0 and count2!=0:#出完全平方后直接结束程序
        print(0)
        break
    count3+=count2#进行累加
    if x == 1:
        break
    if x>i and i==count1+1:
        count3+=1
        break
if x1==1:#（端值单独处理了）
    print(1)
else:
    if count2 % 2 != 0 or count2 == 0:
        if count3 % 2 == 0 and count3 != 0:
            print(1)
        elif x1 == 2 or x1 == 3:#（端值单独处理了）
            print(-1)
        else:
            print(-1)