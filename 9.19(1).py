linenum=int(input())
a=list(range(0,linenum))
x1=list(range(0,linenum))
x2=list(range(0,linenum))
for i in range(linenum):
    a[i]=list(map(float,input().split()))#a[方程序号][第几个变元]
    delta=round(a[i][1]**2-4*a[i][0]*a[i][2],5)
    if delta==0:
        x1[i]=round(-a[i][1]/(2*a[i][0]),5)
        print('x1=x2=',end='')
        print('{:.5f}'.format(x1[i]))
    elif delta<0:
        x1[i] = round(-a[i][1] / (2 * a[i][0]), 5)
        x=round((-delta)**0.5/2/a[i][0],5)
        print('x1=',end='')
        print('{:.5f}'.format(x1[i])+'+',end='')
        print('{:.5f}'.format(x)+'i', end='')
        print(';', end='')
        print('x2=', end='')
        print('{:.5f}'.format(x1[i])+'-', end='')
        print('{:.5f}'.format(x)+'i')
    elif delta>0:
        x1[i] = round(-a[i][1] / (2 * a[i][0]), 7)
        x = round((delta) ** 0.5 / 2 / a[i][0], 7)
        x2[i]=round(x1[i]-x,5)
        x1[i]=round(x1[i]+x,5)
        print('x1='+'{:.5f}'.format(x1[i])+';'+'x2='+'{:.5f}'.format(x2[i]))
        '''import math
n = int(input())
for i in range(n):
    a, b, c = map(float, input().split())
    if b == 0:
        b = -b
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        x1 = format(x1, ".5f")
        x2 = format(x2, ".5f")
        print(f"x1={x1};x2={x2}")
    elif delta == 0:
        t = (-b) / (2 * a)
        x1 = format(t, ".5f")
        print(f"x1=x2={x1}")
    else:
        d = format(math.sqrt(-delta) / (2 * a), ".5f")
        re = format((-b) / (2 * a), ".5f")
        print(f"x1={re}+{d}i;x2={re}-{d}i")'''