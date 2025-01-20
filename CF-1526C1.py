import heapq
from collections import deque
from heapq import heappush, heappop, heapify

x = int(input())
d = list(map(int, input().split()))
health = 0
negheap =[]
ans = 0
for i in range(x):
    health += d[i]
    if d[i] >= 0:
        ans += 1
    else:
        if health < 0:
            if not negheap:
                health-=d[i]
            elif d[i]==negheap[0]:
                health-=d[i]
            else:
                heappush(negheap, d[i])
                health -= heappop(negheap)
        else:
            heappush(negheap, d[i])
            ans += 1
print(ans)