ele=list(range(0,3))
rol=list(range(0,3))
col=list(range(0,3))
for i in range(0,3):
    a,b=map(int,input().split())
    rol[i]=a#行数
    col[i]=b#列数
    ele[i]=list(range(0,a))#第几个列表
    for j in range(0,a):#逐行输入
        ele[i][j]=list(map(int,input().split()))#第一项表示矩阵序号，第二项表示第几行,第三项表示第几列
#运算检查
if col[0]==rol[1] and rol[0]==rol[2] and col[1]==col[2]:
    midans=ele[2]
    for a in range(0,rol[0]):#行
        for b in range(0,col[1]):#列
            for p in range(0,col[0]):
                midans[a][b]+=ele[0][a][p]*ele[1][p][b]#相乘并且求和
            print(midans[a][b],end=' ')
        print('')
else:
    print('Error!')