dir=input()
code=input()
ans=[]
if dir=="R":
    mov=-1
if dir=="L":
    mov=1
len1=list('qwertyuiop')
len2=list('asdfghjkl;')
len3=list('zxcvbnm,./')
ins=list(code)
for x in code:
    if x in len1:
        loc=int(len1.index(x))
        ans.append(len1[loc+mov])
    if x in len2:
        loc=int(len2.index(x))
        ans.append(len2[loc+mov])
    if x in len3:
        loc=int(len3.index(x))
        ans.append(len3[loc+mov])
print(''.join(ans))