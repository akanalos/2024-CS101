n=int(input())
stu=list(enumerate(map(int,input().split())))
stu=sorted(stu,key=lambda a:a[1],reverse=False)
print(' '.join(map(lambda x:str(x[0]+1),stu)))
waittime=0
for i in range(n-1):
    waittime+=stu[i][1]*(n-1-i)
print(f'{waittime/n:.2f}')