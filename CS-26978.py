import heapq

n,k=map(int,input().split())
nums=list(map(lambda u:-1*int(u),input().split()))
l1=nums[0:k]
heapq.heapify(l1)
l2=[]
ans=[-l1[0]]
for x in range(0,n-k):
    heapq.heappush(l1,nums[k+x])
    heapq.heappush(l2, nums[x])
    while l2 and l1[0]==l2[0]:
        heapq.heappop(l1)
        heapq.heappop(l2)
    ans.append(-l1[0])
print(' '.join(str(ele) for ele in ans))