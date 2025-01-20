from collections import deque


def main():
    global n,mountains
    n=int(input())
    mountains=list(map(int,input().split()))
    if n==2:
        if mountains[0]==mountains[1]:
            print(2)
        else:
            print(2)
        return
    else:
        print(visit())
        return
def visit():
    site=deque(sorted([(h,idx) for idx,h in enumerate(mountains)],reverse=False))
    chanceup=[0]*n
    chancedown=[0]*n
    while site:
        (h,l)=site[0]
        p=[]
        while site and site[0][0]==h:
            p.append(site.popleft()[1])
        for ele in p:
            chanceup[ele]+=1
            chancedown[ele]+=1
        for ele in p:
            for x in range(n):
                    if x>ele:
                        chanceup[x]=max(chanceup[x],chanceup[ele])
                    if x<ele:
                        chancedown[x]=max(chancedown[x],chancedown[ele])
    ans=0
    for i in range(n):
        ans=max(chanceup[i]+chancedown[i]-1,ans)
    return ans
main()