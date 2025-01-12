n=int(input())
num=list(map(int,input().split()))
k=int(input())
count=0
for ele in num:
    if k-ele in num and k-ele!=ele:
        count+=1
print(int(count/2))