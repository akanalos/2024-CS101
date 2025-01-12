nums=int(input())
d=[0]*nums
c=[0]*nums
hotel=[]
ans=0
for i in range(nums):
    [d[i],c[i]]=list(map(int,input().split()))
    hotel.append([d[i],c[i]])
z=input()
def D(ele):
    return int(ele[0])
def C(ele):
    return int(ele[1])
con1=sorted(hotel,key=D,reverse=False)
cm=100000001
for i in range(nums):
    if C(con1[i])<=cm:
        cm=C(con1[i])
        ans+=1
print(ans)