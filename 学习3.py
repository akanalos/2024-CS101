#<class 'int'> <class 'float'> <class 'bool'> <class 'complex'>
a = 111
b=isinstance(a, int)
#type()不会认为子类是一种父类类型。
#isinstance()会认为子类是一种父类类型。
c=10
d=b
d=a/c
word = 'Python'
print(word[0], word[5])
print(word[-1], word[-6])
print(b,d)#定义的变量的数据类型是可以被覆盖的
if True:
    print("This will always print")

if not False:
    print("This will also always print")

x = 10
if x:
    print("x is non-zero and thus True in a boolean context")
a = [1, 2, 3, 4, 5, 6]
a[0] = 9
a[2:5] = [13, 14, 15]
a[2:5] = []  # 将对应的元素值设置为 []
print(a)