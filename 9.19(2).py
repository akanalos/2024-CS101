x=int(input())
lucky=[]
i=0
num=[]
att=False
for length in range(1,4):#先讨论位数
    for j in range(0,2**length):#二进制遍历
        s=list(str(bin(j)))
        for let in s[2::]:
            if let == '0':
                num.append('4')
            if let == '1':
                num.append('7')
        for any in range(length-len(num)):#补齐首位‘0’下缺失的4
            num.insert(0,'4')
        a=''.join(num)
        lucky.append(int(a))
        num.clear()
for ele in lucky:
    if x%ele==0:
        att=True
if att:
    print('YES')
else:
    print('NO')