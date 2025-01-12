s=input()
x=0
a=[]
while x<len(s):
    if 'a'<=s[x]<='z':
        a.append(s[x].upper())
    elif 'A'<=s[x]<='Z':
        a.append(s[x].lower())
    else:
        a.append(s[x])
    x=x+1
x=0
while x<len(s):
    print(a[x], end='')
    x=x+1