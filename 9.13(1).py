x=int(input())
ans=0
for num in range(1,x+1):
    ele=str(num)
    list(ele)
    if '7' in ele or num%7==0:
        continue
    else:
        ans+=num**2
print(ans)