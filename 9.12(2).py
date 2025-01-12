x = int(input())
income = []
income = list(map(int, input().split()))
day=1
m=1
for i in range(1,x):
    if income[i]>=income[i-1]:
        day+=1
        if day>m:
            m=day
    else:
        if day>m:
            m=day
        day=1
if day==x:#这个补丁无法挽救递增序列在最后的情况，其实无用
    m=x
print(m)