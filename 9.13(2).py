word=input()
list(word)
he=list('hello')
for x in word:
    if x==he[0]:
        del he[0]
    if len(he)==0:
        print('YES')
        break
if len(he)!=0:
    print('NO')