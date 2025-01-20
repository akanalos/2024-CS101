x=int(input())
a=list(map(int,input().split()))
print(a.count(4)+a.count(3)+(a.count(2)+1)//2+max(0,(a.count(1)-a.count(3)-a.count(2)%2*2+3)//4))