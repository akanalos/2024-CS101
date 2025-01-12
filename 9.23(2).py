a,b=input().split()
x1=int(a)
x2=int(b)
ans=[]
for x in range(x1,x2+1):
    if x==int(list(str(x))[0])**3+int(list(str(x))[1])**3+int(list(str(x))[2])**3:
        ans.append(str(x))
if ans==[]:
    print('NO')
else:
    print(f"{' '.join(ans)}")