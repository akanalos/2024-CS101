
height = [5,4,1,2]
n=len(height)
storage=[(h,idx) for idx,h in enumerate(height)]
storage=sorted(storage,reverse=False,key=lambda u:(u[0],-u[1]))
save=0
start=n
end=0
count=0
lasth=storage[-1][0]+1
while storage:
    h,s=storage.pop()
    if h==0:
        break
    if h!=lasth-1:
        save += (end - start + 1 - count) * (lasth - h-1)
    start=min(start,s)
    end=max(end,s)
    while storage and storage[-1][0]==h:
        h,s=storage.pop()
        count+=1
    count+=1
    start = min(start, s)
    end = max(end, s)
    save+=(end-start+1-count)
    lasth=h
save+=max(lasth-1,0)*(end-start-count+1)
print(save,lasth-1,end-start-count+1)