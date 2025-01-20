n=int(input())
trees=[]
for i in range(n):
    trees.append(list(map(int,input().split())))
trees=sorted(trees,key=lambda x:x[0],reverse=False)
if n<=2:
    print(n)
else:
    ans=2
    for i in range(1,n-1):
        if trees[i][0]-trees[i][1]>trees[i-1][0]:
            ans+=1
        elif trees[i][0]+trees[i][1]<trees[i+1][0]:
            trees[i][0]=trees[i][0]+trees[i][1]
            ans+=1
    print(ans)