x=int(input())
nums=list(bin(x))
ele=nums.copy()
ele=ele[2::]
ans='Yes'
if ele!=ele[-1::-1]:
    ans='No'
print(ans)