word=input()
word=list(word.lower())
ans=''
for x in word:
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u' or x=='y':
        continue
    else:
        ans+='.'+x
print(ans)