import heapq

q=int(input())
pre1=[]
pre2=[]
pre3=[]
pre4=[]
for i in range(q):
    x=list(input().split())
    if x[0]=='+':
        l,r=map(int,x[1:])
        heapq.heappush(pre1,(r,l))
        heapq.heappush(pre2, (-l,-r))
    elif x[0]=='-':
        l,r=map(int,x[1:])
        if pre1 and (r,l)==pre1[0]:
            heapq.heappop(pre1)
            while pre1 and pre3 and (pre1[0] == pre3[0]):
                heapq.heappop(pre3)
                heapq.heappop(pre1)
        else:
            heapq.heappush(pre3,(r,l))
        if pre2 and (-l,-r) == pre2[0]:
            heapq.heappop(pre2)
            while pre2 and pre4 and (pre2[0] == pre4[0]):
                heapq.heappop(pre2)
                heapq.heappop(pre4)
        else:
            heapq.heappush(pre4,(-l,-r))
    if pre1 and pre2 and pre1[0][0]+pre2[0][0]<0:
        print('YES')
    else:
        print('NO')