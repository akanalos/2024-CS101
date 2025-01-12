a=list(map(int,input().split('-')))
delta=int(input())
y=a[0]
m=a[1]
d=a[2]
mon={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}#dict可以比list少写几行
while True:
    if y%4==0:
        if y%100==0:
            if y%400==0:
                mon[2] = 29
            else:
                mon[2] = 28
        else:
            mon[2]=29#我不想讨论闰年qwq
    elif y%4!=0:
        mon[2]=28
    if delta>mon[m]-d:#下一个下月到了
        delta-=mon[m]-d+1
        m+=1
        d=1
    else:#最终留在本月
        d+=delta
        delta=0
    if m==13:#下一年
        m=1
        y+=1
    if delta==0:
        break
m=str(m)
d=str(d)
if len(m)==1:
    m='0'+m#排版工作
if len(d)==1:
    d='0'+d
print(f"{y}-{m}-{d}")