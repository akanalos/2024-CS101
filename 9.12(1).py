x=int(input())
date=[]
for num in range(0,x):
    cin=input()
    list(cin)#转化为单个字符
    c=int(cin[0]+cin[1])#产生所需要的参数
    y=int(cin[2]+cin[3])
    match (cin[4],cin[5]):
        case ('0','1'):
            m=13
            y-=1
        case ('0','2'):
            m=14
            y-=1
        case _:
            m=int(cin[4]+cin[5])
    if y==-1:
        y=99
        c-=1
    d=int(cin[6]+cin[7])
    w=(y+int(y/4)+int(c/4)-2*c+int(26*(m+1)/10)+d-1+700)%7#代入公式计算
    match w:#逐个匹配输出结果
        case 0:
            print('Sunday')
        case 1:
            print('Monday')
        case 2:
            print('Tuesday')
        case 3:
            print('Wednesday')
        case 4:
            print('Thursday')
        case 5:
            print('Friday')
        case 6:
            print('Saturday')