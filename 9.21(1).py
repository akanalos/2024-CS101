x=int(input())#数据数
n=list(range(x))#创建输入列表
s=[]
for j in range(22):
    s.append(2**j)#幂次列表
for i in range(x):
    n[i]=int(input())#输入存入列表
    for k in range(22):
        if 2**k>n[i]:
            end=k-1
            break#寻找输入值对应幂次位置
        elif k==22:
            print('error')
            end=0#纯粹防止end没定义报错
    ans=n[i]*(n[i]+1)/2-2**(end+2)+2#求和后减去2的幂次之和的两倍
    print(int(ans))