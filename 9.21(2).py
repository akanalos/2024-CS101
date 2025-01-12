x=int(input())#数据数
n=list(range(x))#创建输入列表
for i in range(x):
    n[i]=float(input())#输入存入列表
    lines=360/(180-n[i])
    if lines==int(lines):
        print('YES')
    else:
        print('NO')