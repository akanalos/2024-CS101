x=int(input())
income = []
income = list(map(int, input().split()))
day=1
days=[1]
for i in range(1,x):
    if income[i]>=income[i-1]:
        day+=1
        days.append(day)
    else:
        day=1
print(max(days))