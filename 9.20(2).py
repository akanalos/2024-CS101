x=int(input())
ans=list(range(x))
for i in range(x):
    word=list(input())
    if len(word)>10:
        out=[word[0],str(len(word)-2),word[-1]]
        ans[i]=''.join(out)
    else:
        ans[i]=''.join(word)
    print(ans[i])