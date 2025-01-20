ans=[0,1]
def odd(c):
    global l,m,s,ans
    d=1
    while c+d<l and c-d>=0:
        if s[c-d]!=s[c+d]:
            break
        else:
            if m < 2 * d + 1:
                ans = [c - d, c + d + 1]
                m = 2 * d + 1
        d += 1

def even(c):
    global l, m, s,ans
    d = 0
    while c + d + 1 < l and c-d >= 0:
        if s[c - d] != s[c + d +1]:
            break
        else:
            if m < 2 * d +2:
                ans = [c-d,c+d+2]
                m=2*d+2
        d += 1
s=input()
l=len(s)
m=0
for q in range(l):
    odd(q)
    even(q)
print(s[ans[0]:ans[1]])