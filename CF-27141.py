import sys
n=int(input())
value=list(map(lambda u:int(u)-520,input().split()))
dictionary={}
dictionary[0]=0
tot=0
l=0
for i in range(n):
    tot+=value[i]
    if tot in dictionary:
        l=max(l,i+1-dictionary[tot])
    else:
        dictionary[tot]=i+1
print(520*l)