def solve(a,b):
    global t
    if a>=b*2 or a==b:
        return
    else:
        t+=1
        solve(b,a-b)
        return
while True:
    x,y=map(int,input().split())
    if x==0 and y==0:
        break
    else:
        t=0
        solve(max(x,y),min(x,y))
        if t%2==0:
            print('win')
        else:
            print('lose')
