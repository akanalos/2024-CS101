def change(a):
    print(id(a))  # 指向的是同一个对象
    a = 10
    print(id(a))  # 一个新对象
a = 1
print(id(a))
change(a)


def myfunc(n):
    return lambda a: a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))
for x in range(1, 11):
    print('{0:2} {1:3} {2:4'}'.format(x, x*x, x*x*x))