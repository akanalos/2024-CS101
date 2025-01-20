d=int(input())
n=int(input())
moscow=[[0 for i in range(1025+2*d)] for j in range(1025+2*d)]
def refresh(loc):
    for i in range(loc[0],loc[0]+2*d+1):
        for j in range(loc[1], loc[1] + 2 * d+1):
            moscow[j][i]+=loc[2]
count=0
ans=0
for x in range(n):
    refresh(list(map(int,input().split())))
for p in range(d,1025+d):
    for q in range(d,1025+d):
        if moscow[p][q]==ans:
            count+=1
        if moscow[p][q]>ans:
            ans=moscow[p][q]
            count=1
print(count,ans)