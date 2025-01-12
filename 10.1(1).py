'''   a=[1,1]
        for i in range(2,22):
            x=a[i-1]+a[i-2]
            a.append(x)
        print(a)
'''
a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]
nums=int(input())
for i in range(nums):
    x=int(input())
    print(a[x-1])