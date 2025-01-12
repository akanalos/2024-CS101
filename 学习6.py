from random import shuffle
absd={"汉语":"chinese",'英语':"english"}
absd['one']="italy"
absd['挪威']="sweden"
print(absd['one'],absd['挪威'],absd["汉语"])
词典={"汉语":"chinese",'英语':"english"}
print(词典['汉语'],(词典['英语']+"\n")*2)
print (词典.keys())
a={'adjak','dh'}
c={'dh','ajd'}
print(a-c)
x=bytes("WHAT", encoding="utf-8")
print(x,x[0],x[1],x[0::1])
listA=['1','2','3','4',a]
shuffle(listA)
print(listA,'\n',listA[3])
list1 = ['Google', 'Runoob', 'Taobao']
list1.append('Baidu')
print ("更新后的列表 : ", list1);print ("原始列表 : ", list1)
del list1[2]
print ("删除第三个元素 : ", list1)
for x in [1, 2, 3]:
    print(x, end=" ")