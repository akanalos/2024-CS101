def changecases(n,startpoint,endpoint,midpoint):#现在我们需要把n问题递归为n-1
    if n==0:
        return
    changecases(n-1,startpoint,midpoint,endpoint)
    print(f'{startpoint}->{endpoint}')
    changecases(n-1,midpoint,endpoint,startpoint)
n=int(input())
print(2**n-1)
changecases(n,'A','C','B')