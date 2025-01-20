def mtime(n,num):
    if n>=2:
        num=sorted(num,reverse=False)
        s=sum(num)
        u=s
        top=num.pop()
        s-=top
        if top>=s:
            return s
        else:
            return u/2
    elif n==1:
        return 0
while True:
    try:
        n=int(input())
        num=list(map(int,input().split()))
        print(f'{mtime(n,num):.1f}')
    except EOFError:
        break