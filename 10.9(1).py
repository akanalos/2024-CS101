t=23*28*33
t0=28*23
count=1
while True:
    p,e,i,d=map(int,input().split())
    if p==e==i==d==-1:
        break
    else:
        a=p%23
        while a%28!=e%28:
            a+=23
        b=a%33
        while b%33!=i%33:
            a+=t0
            b+=17
        if a>d:
            print(f'Case {count}: the next triple peak occurs in {a-d} days.')
        else:
            print(f'Case {count}: the next triple peak occurs in {a-d+t} days.')
    count+=1