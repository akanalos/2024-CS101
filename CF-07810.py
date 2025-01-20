n=int(input())
for i in range(n):
    x=input()
    if ('19' in x) or int(x)%19==0:
        print('Yes')
    else:
        print('No')