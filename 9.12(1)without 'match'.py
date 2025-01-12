x=int(input())
date=[]
for num in range(0,x):
    cin=input()
    list(cin)#转化为单个字符
    c=int(cin[0]+cin[1])#产生所需要的参数
    y=int(cin[2]+cin[3])
    if cin[4]=='0' and cin[5]=='1':
        m = 13
        y -= 1
    elif cin[4]=='0' and cin[5]=='2':
        m = 14
        y -= 1
    else:
        m = int(cin[4] + cin[5])
    if y == -1:
        y = 99
        c -= 1
    d=int(cin[6]+cin[7])
    w=(y+int(y/4)+int(c/4)-2*c+int(26*(m+1)/10)+d-1+700)%7#代入公式计算
    if w==0:
        print('Sunday')#逐个匹配输出结果
    if w==1:
        print('Monday')
    if w==2:
        print('Tuesday')
    if w==3:
        print('Wednesday')
    if w==4:
        print('Thursday')
    if w==5:
        print('Friday')
    if w==6:
        print('Saturday')