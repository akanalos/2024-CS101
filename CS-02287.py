while True:
    n=int(input())
    if n==0:
        break
    else:
        tj=[]
        dw=[]
        money=0
        tj.extend(list(map(int,input().split())))
        dw.extend(list(map(int,input().split())))
        tj=sorted(tj,reverse=False)
        dw=sorted(tj,reverse=False)
        while n>0:
            if tj[0]>dw[0]:
                money+=200
                del tj[0]
                del dw[0]
                n-=1
                tj=tj[:]
                dw=dw[:]
            elif tj[-1]>dw[-1]:
                del tj[-1]
                del dw[-1]
                n-=1
                money += 200
                tj = tj[:]
                dw = dw[:]
            elif tj[0]<dw[0]:
                del tj[0]
                del dw[-1]
                n -= 1
                money-=200
                tj = tj[:]
                dw = dw[:]
            else:
                if tj[0]==dw[-1]:
                    del tj[0]
                    del dw[-1]
                    n-=1
                    tj = tj[:]
                    dw = dw[:]
                elif tj[0]>dw[-1]:
                    del tj[0]
                    del dw[-1]
                    n -= 1
                    money+=200
                    tj = tj[:]
                    dw = dw[:]
                else:
                    money-=200
                    n-=1
                    del tj[0]
                    del dw[-1]
                    tj = tj[:]
                    dw = dw[:]
            if n == 0:
                break
        print(money)


