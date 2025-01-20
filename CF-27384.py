# pylint: skip-file
n,k=map(int,input().split())
a=list(map(int,input().split()))
case=[]
for i in range(n):
    case.append((a[2*i],a[2*i+1]-1))
case=sorted(case,reverse=False)
winner=tuple(map(lambda u:int(u)-1,input().split()))
votes=[0]*314159
de=0
at=0
idd=winner[0]
t=0
print(case)
if k==314159:
    print(case[-1][0]-case[0][0])
else:
    for j in range(n):
        votes[case[j][1]]+=1
        if case[j][1] in winner:
            if case[j][1]==idd:
                de+=1
                for ele in winner:
                    if votes[ele]<de:
                        de=votes[ele]
                        idd=ele
            else:
                pass
        else:
            at=max(at,votes[case[j][1]])
        if at>=de:
            continue
        else:
            if j!=n-1:
                t+=case[j+1][0]-case[j][0]
                print(case[j],t)
    print(t)