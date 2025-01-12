sock,interval=map(int,input().split())
Day=0
while True:
    Day+=1#a new day starts
    sock-=1#wear a pair of socks
    if sock<0:#if he still has a sock
        print(Day-1)
        break
    if Day%interval==0:#if he gets a pair at night
        sock+=1