while True:
    r,n=map(int,input().split())
    if r==-1 and n==-1:
        break
    x=list(map(int,input().split()))
    x=sorted(x,reverse=False)
    cover=-10000
    stone=0
    l=len(x)
    i=0
    while i<l:
        if cover+r>=x[i]:
            i+=1
        else:
            if i==l-1:
                stone+=1
                i+=1
                break
            else:
                j=i
                while x[j]+r>=x[i]:
                    if i==l-1:
                        i+=1
                        break
                    else:
                        i+=1
                cover=x[i-1]
                stone+=1
    print(stone)

