while True:
    try:
        a,b=input().split()
        a=int(a)
        b=int(b)
        for i in range(a,0,-1):
            if a%i==0 and b%i==0:
                print(i)
                break
    except EOFError:
        break
