def D(ele):
    return int(ele[0])
def C(ele):
    return int(ele[1])
while True:
    nums=int(input())
    if nums==0:
        break
    d=[0]*nums
    c=[0]*nums
    hotel=[]
    ans=0
    for i in range(nums):
        [d[i],c[i]]=list(map(int,input().split()))
        hotel.append([d[i],c[i]])
    con1=sorted(hotel, key=lambda x:(D(x),C(x)), reverse=False)
    cm=100000001
    for i in range(nums):
        if C(con1[i])<cm:
            cm=C(con1[i])
            ans+=1
    print(ans)