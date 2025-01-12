from bisect import bisect_left, bisect
x=int(input())
s1,s2=0,0
loc1=[]
loc2=[0]
for i in range(1,35000):
    loc1.append(s2)#1到i的序列开始索引在列表中索引为i
    s1+=len(str(i))
    s2+=s1
    loc2.append(s1)#1~i的数列长度
for i in range(x):
    pos=int(input())
    if pos==1 or pos==2:
        print(1)
    elif pos==3:
        print(2)
    else:
        loc=bisect_left(loc1,pos)-1#pos-1为索引值，这找出了完整序列，loc给出了索引
        offset=pos-loc1[loc]#余下部分的长度
        loc=bisect_left(loc2,offset)-1#在1~loc后的一个数
        offset-=loc2[loc]#最终剩长
        print(str(loc+1)[offset-1])